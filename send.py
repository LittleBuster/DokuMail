<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>NewsBaloon</class>
 <widget class="QWidget" name="NewsBaloon">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>560</width>
    <height>141</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>560</width>
    <height>141</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>560</width>
    <height>141</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Новость</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>images/news.ico</normaloff>images/news.ico</iconset>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>-80</x>
     <y>-80</y>
     <width>751</width>
     <height>261</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap>images/baloon.png</pixmap>
   </property>
   <property name="alignment">
    <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop</set>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>0</y>
     <width>151</width>
     <height>41</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>28</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#00ff5f;&quot;&gt;Новость&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop</set>
   </property>
  </widget>
  <widget class="QLineEdit" name="leTitle">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>60</y>
     <width>531</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>15</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">QLineEdit {
	background-color: rgba(23, 115, 255, 137);
	color:rgb(255, 255, 255);
	border-width: 1px;
	border-color: rgb(255, 255, 255);
     border-style: solid;
     border-radius: 5px;
}</string>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="readOnly">
    <bool>true</bool>
   </property>
  </widget>
  <widget class="QLabel" name="label_21">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>37</y>
     <width>111</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial Black</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; color:#00fffa;&quot;&gt;Заголовок:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pbRead">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>100</y>
     <width>381</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">QPushButton {
	background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(0, 29, 203, 255), stop:1 rgba(190, 255, 255, 255));
	color:rgb(255, 255, 255);
	border-width: 1px;
     border-style: solid;
     border-radius: 10px;
	min-width: 80px;
}

QPushButton:hover {
    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(82, 100, 203, 255), stop:1 rgba(190, 255, 255, 255));
}

QPushButton:pressed {
    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.596154 rgba(85, 250, 255, 255), stop:1 rgba(190, 255, 255, 255));
}</string>
   </property>
   <property name="text">
    <string>Читать новость</string>
   </property>
   <property name="icon">
    <iconset>
     <normaloff>images/news.ico</normaloff>images/news.ico</iconset>
   </property>
   <property name="iconSize">
    <size>
     <width>20</width>
     <height>20</height>
    </size>
   </property>
  </widget>
  <widget class="QPushButton" name="pbClose">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>100</y>
     <width>141</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">QPushButton {
	background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(0, 29, 203, 255), stop:1 rgba(190, 255, 255, 255));
	color:rgb(255, 255, 255);
	border-width: 1px;
     border-style: solid;
     border-radius: 10px;
	min-width: 80px;
}

QPushButton:hover {
    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(82, 100, 203, 255), stop:1 rgba(190, 255, 255, 255));
}

QPushButton:pressed {
    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.596154 rgba(85, 250, 255, 255), stop:1 rgba(190, 255, 255, 255));
}</string>
   </property>
   <property name="text">
    <string>Закрыть</string>
   </property>
   <property name="icon">
    <iconset>
     <normaloff>images/exit.png</normaloff>images/exit.png</iconset>
   </property>
   <property name="iconSize">
    <size>
     <width>20</width>
     <height>20</height>
    </size>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
