originalImage = imread('Enter you image path here');
originalImage = im2double(originalImage); 
[rows, cols, ~] = size(originalImage);
[x, y] = meshgrid(1:cols, 1:rows);
frequency = 20; 
periodicNoise = 0.1 * sin(2 * pi * frequency * x / cols) + ...
                0.1 * sin(2 * pi * frequency * y / rows);

noisyImage = originalImage;
for channel = 1:size(originalImage, 3)
    noisyImage(:, :, channel) = originalImage(:, :, channel) + periodicNoise;
end
noisyImage = min(max(noisyImage, 0), 1);
figure;
subplot(1, 2, 1);
imshow(originalImage);
title('Original RGB Image');
subplot(1, 2, 2);
imshow(noisyImage);
title('Image with Periodic Noise');
