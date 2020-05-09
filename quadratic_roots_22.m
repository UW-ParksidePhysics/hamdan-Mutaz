a = input('Enter a value for a: ')
b = input('Enter a value for b: ')
c = input('Enter a value for c: ')

disc = b*b - 4*a*c;
d = sqrt(disc)

if disc < 0
disp('Warning: discriminant is negative, roots are imaginary');
d=sqrt(d^2)
x1_imaginary= (-b-d)/(2*a)
x2_imaginary= (-b+d)/(2*a)

elseif disc == 0
    disp('Discriminant is zero, roots are repeated')
    xZero= -b/(2*a)
    disp(xZero)
else disc > 0
     d = sqrt(disc);
    x1 = (-b - d) / (2 * a);
    x2 = (2 * c) / (-b - d);
    R = [x1, x2];
    disp('roots are:')
    disp(R)
end
