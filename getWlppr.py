#! /usr/bin/python
import urllib2
import re
import time
import os
import getpass

def get_html(url):

  connection = urllib2.urlopen(url)
  data = connection.read()

  return data

def get_images( html_data , base_url ):

  #print( "html_data is : %s" % html_data)
  index_begin = html_data.find('g_img={url')
  index_end = index_begin + 300

  #print( "index begin %s index end %s "%(index_begin,index_end))

  tmp_str = html_data[index_begin:index_end]
  #print( "TMP str is %s : " % tmp_str )

  index_begin_2 = tmp_str.find('"')
  index_end_2 = tmp_str.find("jpg")

  tmp_str2 = tmp_str[index_begin_2+1:index_end_2 + 3]

  print("tmp str 2 is %s"%tmp_str2)

  return get_html( base_url + "/" + tmp_str2 )

def main():

  base_url = "http://bing.com"
  html_data = get_html(base_url)

  images = get_images( html_data , base_url )

  if images != None and len( images ) > 0:
      # find with help of regular expression path to image
      filename = '/home/%s/Downloads/Img%s.jpg'%( getpass.getuser() , time.strftime("%Y-%m-%d") )
      f 	   = open(filename, "w")
      f.write(images)
      f.close()
      print("Saved as %s"%filename)
      os.system("notify-send ""%s""" % filename)
      os.system("eom %s"%filename)

	#os.system(str("xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitor0/image-path --set %s " % '/home/yevgen/YandexImages/Img'+time.strftime("%Y-%m-%d")+'.jpeg'))


main()
