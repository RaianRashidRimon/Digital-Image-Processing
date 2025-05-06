img = imread('Enter your image path here');
edgesR = edge(img(:, :, 1), 'Canny');
edgesG = edge(img(:, :, 2), 'Canny');
edgesB = edge(img(:, :, 3), 'Canny');
edges = edgesR | edgesG | edgesB;
[H, T, R] = hough(edges);
P = houghpeaks(H, 5, 'threshold', ceil(0.3 * max(H(:))));
lines = houghlines(edges, T, R, P, 'FillGap', 5, 'MinLength', 7);
figure;
imshow(img), hold on;
for k = 1:length(lines)
    xy = [lines(k).point1; lines(k).point2];
    plot(xy(:,1), xy(:,2), 'LineWidth', 2, 'Color', 'green');
    plot(xy(1,1), xy(1,2), 'x', 'LineWidth', 2, 'Color', 'yellow');
    plot(xy(2,1), xy(2,2), 'x', 'LineWidth', 2, 'Color', 'red');
end
title('Detected Lines');
hold off;
