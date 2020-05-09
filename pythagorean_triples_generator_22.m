file = fopen('pythagorean_triples.txt', 'wt')
    for a=1:1000
        for b=1:1000
            for c=1:1000
                if c == sqrt(a^2  + b^2)
                    fprintf('(%g,%g,%g)\n',a,b,c')
                end
            end
        end
    end
fclose(file);

type pythagorean_triples.txt
