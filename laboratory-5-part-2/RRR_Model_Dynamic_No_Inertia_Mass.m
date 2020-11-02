% Copyright (C) 1993-2014, by Peter I. Corke
%
% This file is part of The Robotics Toolbox for MATLAB (RTB).
% 
% RTB is free software: you can redistribute it and/or modify
% it under the terms of the GNU Lesser General Public License as published by
% the Free Software Foundation, either version 3 of the License, or
% (at your option) any later version.
% 
% RTB is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU Lesser General Public License for more details.
% 
% You should have received a copy of the GNU Leser General Public License
% along with RTB.  If not, see <http://www.gnu.org/licenses/>.
%
% http://www.petercorke.com

clear L
deg = pi/180;

% joint angle limits from 
% A combined optimization method for solving the inverse kinematics problem...
% Wang & Chen
% IEEE Trans. RA 7(4) 1991 pp 489-

L(1) = Revolute( ...
    'd', 1,  ...
    'a', 0,  ...
    'alpha', -pi/2, ...
    'I', [0, 0, 0, 0, 0, 0], ...
    'm', 0, ...
    'Jm', 1e-4, ...
    'G', 500, ...
    'B', 10*1e-4, ...
    'qlim', [-180 180]*deg );

L(2) = Revolute( ...
    'd', 0, ...
    'a', 1, ...
    'alpha', 0,  ...
    'I', [0, 0, 0, 0, 0, 0], ...
    'm', 0, ...
    'Jm', 1e-4, ...
    'G', 500, ...
    'B', 10*1e-4, ...
    'qlim', [-90 90]*deg );

L(3) = Revolute( ...
    'd', 0, ...
    'a', 1, ...
    'alpha', 0,  ...
    'I', [0, 0, 0, 0, 0, 0], ...
    'm', 0, ...
    'Jm', 1e-4, ...
    'G', 500, ...
    'B', 10*1e-4, ...
    'qlim', [-90 90]*deg);

% L(4) = Revolute('d', 0, 'a', 0, 'alpha', 0, 'm', 1);

RRR_robot = SerialLink(L, 'name', 'RRR Robot', 'gravity', [0, 0, 10]);

q_load1 = [0 0 pi/2];
q_load2 = [0 0 0];

clear L

figure(1)
% RRR_robot.teach('eul')

RRR_robot.plot(q_load2)
% taug = RRR_robot.gravload(q_load2)
