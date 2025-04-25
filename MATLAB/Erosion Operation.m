originalImage = imread('Enter your image path here');
if size(originalImage, 3) == 3
    binaryImage = imbinarize(rgb2gray(originalImage));
else
    binaryImage = imbinarize(originalImage);
end
se = strel('disk', 9);
erodedImage = imerode(binaryImage, se);
figure;
subplot(1, 2, 1);
imshow(binaryImage);
title('Original Binary Image');
subplot(1, 2, 2);
imshow(erodedImage);
title('Eroded Image');
