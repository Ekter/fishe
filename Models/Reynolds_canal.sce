// Estimation de Nombre de Reynolds à l'echelle de canal hydraulique 

clear ; 

nu = 10^(-6) ; // [ m^2 / s ] viscosité cinematique 

h = (157 - 86) / 1000 ; // [m] profondeur de l'écoulement  
b = 54.4 / 1000  ; // [m] largeur de canal

A = h * b  ; // [m^2] surface mouillée 
P = 2 * h + b ; // [m] perimetre mouillé
Rh = A / P ; // [m] rayon hydraulique 
Dh = 4 * Rh  ; // [m] diametre hydraulique 
Q = 0.65 / 1000 ; // [m^3/s] débit volumique 
U = Q / A ; // [m/s] Vitesse moyenne de l'écoulement
Re = Dh * U / nu ; // nombre de Reynolds 
disp( "Re = " , Re , " il est bien turbulent")



