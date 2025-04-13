img = imread('/MATLAB Drive/noisy_image.jpg');
filterSize = 10;
sigma = 15;
h = fspecial('gaussian', filterSize, sigma);
[rows, cols, numChannels] = size(img);
filteredImg = zeros(rows, cols, numChannels, 'like', img);
for channel = 1:numChannels
    filteredImg(:, :, channel) = imfilter(img(:, :, channel), h, 'replicate');
end
figure('Position', [100, 100, 600, 800]);
subplot(2, 1, 1);
imshow(img);
title('Original Image');
subplot(2, 1, 2);
imshow(filteredImg);
title('Filtered Image with Gaussian Filter');
