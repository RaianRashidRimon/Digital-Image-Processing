originalImage = imread('Enter your image path here');
originalImage = im2double(originalImage);
noisyImage = imnoise(originalImage, 'salt & pepper', 0.5);
figure;
subplot(1, 2, 1);
imshow(originalImage);
title('Original Image');

subplot(1, 2, 2);
imshow(noisyImage);
title('Image with Salt & Pepper Noise');
