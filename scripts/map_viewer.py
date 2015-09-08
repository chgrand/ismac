#!/usr/bin/env python

from copy import copy
import time
from PySide import QtGui, QtCore


##########

#Graphical parameters

comMaxOpacity = 0.5
comTrailLength = 5. # in sec


posTrailMaxOpacity = 0.5
posTrailLength = 60 #in sec
posTrailStep = 5 #in sec
##########

class MapViewer(QtGui.QWidget):

    def __init__(self, parent):
        super(MapViewer, self).__init__(parent)

    def init(self, a_map, x_0, y_0, x_size, y_size, cb_click=None):
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
        
        self.opacity = 0.7
        
        self.cb_click = cb_click #Callback for displaying x,y when clicked
        
        self.draw_coms = True
        self.draw_trails = True
        self.coms = [] # List of dict
        self.past_pos = {} #Each key is a robot, each value a list of dict
    
    def set_opacity(self, value):
        v = float(value)/100  #Assume value in %
        if v <= 1 and v >=0:
            self.opacity = v
            self.update()
        else:
            print("%s is not a valid opacity" % value)
    
    def set_draw_com(self, b):
        if b:
            print("Drawing the coms")
        else:
            print("Stop drawing the coms")
        self.draw_coms = b
        
    def set_draw_trail(self, b):
        if b:
            print("Drawing the trails")
        else:
            print("Stop drawing the trails")
        self.draw_trails = b
        
    def add_com(self, robotFrom, robotTo, color="green"):
        self.coms.append({"from":robotFrom, "to":robotTo, "time":time.time(), "color":color})
    
    def add_agent(self, agent):
        self.agents_list.append(agent)
        agent.set_gui(self)
        
    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.save()
        scale_ = self.viewport_factor*self.zoom_factor
        painter.setOpacity(self.opacity)
        painter.scale(scale_, scale_)
        painter.translate(-self.viewport_origin_x, -self.viewport_origin_y)
        painter.drawImage(0, 0, self.map_image)
        painter.restore()    

        pos = {}
        current_time = time.time()

        for agent in self.agents_list:
            agent_name = agent.get_name()
            (x, y) = self.viewport_from_map_mt( *agent.get_pos() )
            color = QtGui.QColor(agent.getColor())
            pen = QtGui.QPen(color, 3, QtCore.Qt.SolidLine)            
            painter.setPen(pen)
            self.plotMark(painter, x, y)
            painter.save()
            painter.save()
            
            # Draw the trail
            if self.draw_trails and agent_name in self.past_pos:
                l = copy(self.past_pos[agent_name])
                l.append({"time":current_time, "pos":agent.get_pos()})
                for d1,d2 in zip(l,l[1:]):
                    opacity = posTrailMaxOpacity * (1 - (current_time - d1["time"])/posTrailLength)
                    painter.setOpacity(opacity)
                    (x1_past, y1_past) = self.viewport_from_map_mt( *d1["pos"] )
                    (x2_past, y2_past) = self.viewport_from_map_mt( *d2["pos"] )
                    painter.drawLine(x1_past, y1_past, x2_past, y2_past)

            painter.restore()

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
            
            pos[agent.get_name()] = (x,y)
            
            
            if agent_name not in self.past_pos:
                self.past_pos[agent_name] = []
            # Keep it only it if is posTrailStep seconds after the last position
            if not self.past_pos[agent_name] or current_time > self.past_pos[agent_name][-1]["time"] + posTrailStep:
                if agent.get_pos()[0] != 0 or agent.get_pos()[1] != 0:
                    self.past_pos[agent_name].append({"time":current_time, "pos":agent.get_pos()})
            # Remove the obsolete past positions
            self.past_pos[agent_name] = [d for d in self.past_pos[agent_name] if current_time < d["time"] + posTrailLength]
            
        
        if self.draw_coms:
            for d in self.coms:
                r1,r2 = d["from"],d["to"]
                color = QtGui.QColor(QtGui.QColor(d["color"]))
                pen = QtGui.QPen(color, 3, QtCore.Qt.SolidLine)            
                painter.setPen(pen)
                painter.setOpacity(comMaxOpacity * (1 - (current_time - d["time"])/comTrailLength))
                painter.drawLine(pos[r1][0], pos[r1][1], pos[r2][0], pos[r2][1])
                
            self.coms = [d for d in self.coms if current_time < d["time"] + comTrailLength]
        
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
            if self.cb_click is not None:
                self.cb_click(x,y)
            
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



