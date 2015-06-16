#!/usr/bin/env python

#import rospy
#from sensor_msgs.msg import NavSatFix
#from geometry_msgs.msg import PoseStamped
import os, sys
from PySide import QtGui, QtCore

class Viewer(QtGui.QWidget):

    def __init__(self, a_map, x_0, y_0, x_size, y_size):
        super(Viewer, self).__init__()

        self.map_image = a_map
        # Relation between map pixel and meters
        self.map_mt_origin_x = x_0
        self.map_mt_origin_y = y_0
        self.map_mt_factor = float(self.map_image.width()) / float(x_size)

        # Relation between map coords in px and viewport coords
        self.viewport_origin_x = 0
        self.viewport_origin_y = 0
        self.viewport_factor = 1.0
        self.zoom_factor = 1.0
        self.updateScaling()

        # Agents
        self.agents_list = []

        # IHM action
        self.move_map = False

        # Create widget
        self.setGeometry(200, 200, 500, int(y_size*500/x_size))
        self.setWindowTitle('ISMAC')
        self.show()

                
    def add_agent(self, agent):
        self.agents_list.append(agent)
        agent.set_gui(self)
        
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.save()
        scale_ = self.viewport_factor*self.zoom_factor
        painter.setOpacity(.7)
        painter.scale(scale_, scale_)
        painter.translate(-self.viewport_origin_x, -self.viewport_origin_y)
        painter.drawImage(0, 0, self.map_image)
        painter.restore()    

        for agent in self.agents_list:
            (x, y) = self.viewport_from_map_mt( *agent.get_pos() )
            color = QtGui.QColor(agent.getColor())
            pen = QtGui.QPen(color, 3, QtCore.Qt.SolidLine)            
            painter.setPen(pen)
            self.plotMark(painter, x, y)
            painter.save()

            # draw text in bounding box
            painter.setFont(QtGui.QFont('Monospace', 12))
            rect = painter.boundingRect(QtCore.QRect(x+12,y-8,0,0),
                                        QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom,
                                        agent.get_name())
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(QtCore.Qt.white)
            painter.save()
            painter.setOpacity(.5)
            painter.drawRect(rect)
            painter.restore()
            painter.setPen(QtCore.Qt.black)
            painter.drawText(x+12, y-12, agent.get_name())
            painter.restore()
            
        painter.end()

    def plotMark(self, painter, x, y, mark='x', size=12):
        half_size = int(size/2)
        if (mark=='x') or (mark=='X') :
            painter.drawLine(x-half_size, y-half_size, x+half_size, y+half_size)
            painter.drawLine( x-half_size, y+half_size, x+half_size, y-half_size)
            
    def resizeEvent(self, event):
        self.updateScaling()

    def wheelEvent(self, event):
        (x_vp, y_vp) = (event.x(), event.y())
        (x_map, y_map) = self.map_px_from_viewport(x_vp, y_vp)
        if event.delta()>0 :
            if(self.zoom_factor<10.0) :
                self.zoom_factor+=0.5
        else:
            if(self.zoom_factor>1.0) :
                self.zoom_factor-=0.5

        factor = self.viewport_factor * self.zoom_factor
        self.viewport_origin_x = int(x_map-x_vp/factor)
        self.viewport_origin_y = int(y_map-y_vp/factor)

        if self.viewport_origin_x < 0:
            self.viewport_origin_x = 0
        if self.viewport_origin_y < 0:
            self.viewport_origin_y = 0

        if self.zoom_factor==1.0:
            self.viewport_origin_x = 0
            self.viewport_origin_y = 0
        self.update()

    def mouseMoveEvent(self, event):
        (x_vp, y_vp) = (event.x(), event.y())
        (x_map, y_map) = self.map_px_from_viewport(x_vp, y_vp)
        
        if (event.buttons()==2) and (self.move_map==True):
            dx = x_map - self.move_pos_x
            dy = y_map - self.move_pos_y
            self.viewport_origin_x -= dx
            self.viewport_origin_y -= dy
            self.update()
    
    def mousePressEvent(self, event):
        (x_vp, y_vp) = (event.x(), event.y())
        (x_map, y_map) = self.map_px_from_viewport(x_vp, y_vp)

        if event.button()==2:
            self.move_pos_x = x_map
            self.move_pos_y = y_map
            self.move_map = True
                
    def mouseReleaseEvent(self, event):
        if event.button()==1:
            (x, y) = self.map_mt_from_viewport(event.x(), event.y())
            x = int(x*100)/100.
            y = int(y*100)/100.
            print("Goto point: "),
            print((x,y))
            
        if event.button()==2:
            self.move_map = False
        
    def updateScaling(self):
        scale_w = float(self.width()) / self.map_image.width()
        scale_h = float(self.height()) / self.map_image.height()
        if scale_w < scale_h:
            self.viewport_factor = scale_w
        else:
            self.viewport_factor = scale_h
        #print("scale="),
        #print(self.viewport_factor)
        
    def map_px_from_viewport(self, x, y):
        scale_factor = self.viewport_factor*self.zoom_factor        
        return ( int(x/scale_factor+self.viewport_origin_x),
                 int(y/scale_factor+self.viewport_origin_y))

    def map_px_from_map_mt(self, x,y):
        return ( int(+(x-self.map_mt_origin_x)*self.map_mt_factor),
                 int(-(y-self.map_mt_origin_y)*self.map_mt_factor))
    
    def map_mt_from_viewport(self, x, y):
        (x_map, y_map) = self.map_px_from_viewport(x, y)
        return ( float(+x_map/self.map_mt_factor + self.map_mt_origin_x),
                 float(-y_map/self.map_mt_factor + self.map_mt_origin_y))

    def viewport_from_map_mt(self, x, y):
        (x_px, y_px) = self.map_px_from_map_mt(x,y)
        scale_factor = self.viewport_factor*self.zoom_factor
        return ( (x_px - self.viewport_origin_x)*scale_factor,
                 (y_px - self.viewport_origin_y)*scale_factor)



