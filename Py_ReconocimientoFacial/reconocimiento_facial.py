import cv2
import face_recognition as fr 

#Cargar imagenes
foto_control = fr.load_image_file('FotoA.jpg')
foto_prueba = fr.load_image_file('FotoB.jpg')

#BGR to RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGBA)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGBA)

#Localizar cara control
lugar_cara_A =fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

print(lugar_cara_A)


#Mostrar imagenes 

cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

#Mantener programa abierto
cv2.waitKey(0)