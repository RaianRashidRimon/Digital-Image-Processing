originalImage = imread('Enter your image path here');
if size(originalImage, 3) == 3
    binaryImage = imbinarize(rgb2gray(originalImage));
else
    binaryImage = imbinarize(originalImage);
end
se = strel('disk', 8);
openedImage = imopen(binaryImage, se);
closedImage = imclose(binaryImage, se);
figure;
subplot(1, 3, 1);
imshow(binaryImage);
title('Original Binary Image');
subplot(1, 3, 2);
imshow(openedImage);
title('Opened Image');
subplot(1, 3, 3);
imshow(closedImage);
title('Closed Image');
