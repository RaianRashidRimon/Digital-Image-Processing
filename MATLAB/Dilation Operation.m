originalImage = imread('C:\Users\CSELAB-2\Desktop\403 DIP lab 7\ryse.jpg');
if size(originalImage, 3) == 3
    binaryImage = imbinarize(rgb2gray(originalImage));
else
    binaryImage = imbinarize(originalImage);
end
se = strel('disk', 2);
dilatedImage = imdilate(binaryImage, se);
figure;
subplot(1, 2, 1);
imshow(binaryImage);
title('Original Binary Image');
subplot(1, 2, 2);
imshow(dilatedImage);
title('Dilated Image');