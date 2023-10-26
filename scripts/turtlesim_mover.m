%%
rosshutdown;
rosinit('http://LAPTOP-B6O42SIN:11311/'); %Conexion con nodo maestro
%rosinit('http://ubuntu:11311/');
%%
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); %Creacion publicador
velMsg = rosmessage(velPub); %Creaci´on de mensaje
%%

velMsg.Linear.X = 1; %Valor del mensaje
send(velPub,velMsg); %Envio
pause(1)
velx=1;
vely=1;
escala=1;
velx1=1*escala;
vely1=1*escala;
velx2=-1*escala;
vely2=-1*escala;
posesub = rossubscriber("/turtle1/pose","DataFormat","struct")
while(1)
    posedata = receive(posesub,10)

    velMsg.Linear.X = velx; %Valor del mensaje
    velMsg.Linear.Y = vely;
    posex = posedata.X
    posey = posedata.Y
    if(posex>=10 ) 
        velx=velx2;
    elseif posex<=2
        velx=velx1;
    end
    if(posey>=10 ) 
        vely=vely2;
    elseif posey<=2
        vely=vely1;
    end

    send(velPub,velMsg); %Envio
    
    pause(0.2)
end
