img = imread('/MATLAB Drive/noisy_image.jpg');
filterSize = 3;
h = fspecial('average', filterSize);
[rows, cols, numChannels] = size(img);
filteredImg = zeros(rows, cols, numChannels, 'like', img);
for channel = 1:numChannels
    filteredImg(:, :, channel) = imfilter(img(:, :, channel), h, 'replicate');
end
figure;
subplot(1, 2, 1);
imshow(img);
title('Original Image');
subplot(1, 2, 2);
imshow(filteredImg);
title('Filtered Image with Mean Filter');
