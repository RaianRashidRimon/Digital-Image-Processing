inputImage = imread('Enter the path to the image here');
if size(inputImage, 3) == 3
    grayImage = rgb2gray(inputImage);
else
    grayImage = inputImage;
end
figure;
subplot(2,2,1);
imshow(grayImage);
title('Original Grayscale Image');
subplot(2,2,2);
imhist(grayImage);
title('Histogram of Original Image');
equalizedImage = histeq(grayImage);
subplot(2,2,3);
imshow(equalizedImage);
title('Histogram Equalized Image');
subplot(2,2,4);
imhist(equalizedImage);
title('Histogram of Equalized Image');