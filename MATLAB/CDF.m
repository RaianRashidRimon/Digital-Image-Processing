inputImage = imread('Enter the path to the image here');
if size(inputImage, 3) == 3
    grayImage = rgb2gray(inputImage);
else
    grayImage = inputImage;
end
[counts, grayLevels] = imhist(grayImage);
cdf = cumsum(counts) / numel(grayImage);
figure;
subplot(2,2,1);
imshow(grayImage);
title('Grayscale Image');
subplot(2,2,2);
bar(grayLevels, counts, 'BarWidth', 1);
title('Histogram of Grayscale Image');
xlabel('Gray Level');
ylabel('Frequency');
subplot(2,2,3);
plot(grayLevels, cdf, 'LineWidth', 2);
title('CDF of Grayscale Image');
xlabel('Gray Level');
ylabel('Cumulative Probability');
subplot(2,2,4);
imshow(grayImage);
title('Original Grayscale Image');