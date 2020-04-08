diary on

A = [1 2 3; 3 3 4; 2 3 3];
b = [1; 1; 2];
x = A\b

x=0:pi/100:2*pi;
y1 = 2*cos(x);
y2 = cos(x);
y3 = 0.5*cos(x);
plot(x,y1,'--',x,y2,'-',x,y3,':')
xlabel('0 \leq x \leq 2\pi')
ylabel('Cosine functions')
legend('2*cos(x)','cos(x)','0.5*cos(x)')
title('Typical example of multiple plots')
axis([0, 2*pi, -3, 3])

f = factorial(5)

% This script file calculates the average of points
% scored in three games.
% The point from each game are assigned to a variable
% by using the 'input' command.
game1 = input('Enter the points scored in the first game ');
game2 = input('Enter the points scored in the second game ');
game3 = input('Enter the points scored in the third game ');
average = (game1+game2+game3)/3

A = [3 12 1; 12 0 2; 0 2 3];
b = [2.36; 5.26; 2.77];
x = A\b;
disp('Apples, Bananas and Cantaloupe are priced as follows')
fprintf('$%.2f \n', x)

F = input('Enter Temperature in F');
C = 5/9*(F-32);
fprintf('That is equivalent to %.2f Degrees C', C)

disp('Enter Persons Height and Weight in Feet, Inches and Pounds');
Feet = input('Enter Feet');
Inches = input('Enter Inches');
Weight = input('Enter Pounds');
Height = Feet*12+Inches;
Kilogram = Weight*0.453592;
Centimeters = Height*2.54;

fprintf('The Persons Height is %.2f Centimeters\n', Centimeters)
fprintf('The Persons Weight is %.2f kg', Kilogram)

diary off 
