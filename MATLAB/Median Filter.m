inputImage = imread('Enter your image path here');
filterSize = 3;
[rows, cols, numChannels] = size(inputImage);
filteredImage = zeros(rows, cols, numChannels, 'like', inputImage);
for channel = 1:numChannels
    filteredImage(:, :, channel) = medfilt2(inputImage(:, :, channel), [filterSize filterSize]);
end
figure('Position', [100, 100, 600, 800]); 
subplot(2, 1, 1);
imshow(inputImage);
title('Original Image');
subplot(2, 1, 2);
imshow(filteredImage);
title('Filtered Image of Median Filter');
imwrite(filteredImage, 'filtered_image.jpg');
