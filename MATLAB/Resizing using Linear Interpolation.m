img = imread('Enter the path to the image here');
scaleX = 6; 
scaleY = 4;
[originalRows, originalCols, numChannels] = size(img);
newRows = round(originalRows * scaleY);
newCols = round(originalCols * scaleX);
[x, y] = meshgrid(1:newCols, 1:newRows);
origX = (x - 0.5) / scaleX + 0.5;
origY = (y - 0.5) / scaleY + 0.5;
resizedImg = zeros(newRows, newCols, numChannels, 'like', img);
for channel = 1:numChannels
    resizedImg(:, :, channel) = interp2(double(img(:, :, channel)), origX, origY, 'linear');
end
resizedImg = uint8(resizedImg);
figure('Position', [100, 100, 600, 800]);
subplot(2, 1, 1);
imshow(img);
title('Original Image');
subplot(2, 1, 2);
imshow(resizedImg);
title('Resized Image with Linear Interpolation');

