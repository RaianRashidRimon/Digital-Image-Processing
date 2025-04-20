img = imread('Enter your image path here');
skipFactor = 15; 
[rows, cols, numChannels] = size(img);
outputRows = ceil(rows / skipFactor);
outputCols = ceil(cols / skipFactor);
skippedImg = zeros(outputRows, outputCols, numChannels, 'like', img);
for channel = 1:numChannels
    skippedImg(:, :, channel) = img(1:skipFactor:end, 1:skipFactor:end, channel);
end
figure('Position', [100, 100, 600, 800]);
subplot(2, 1, 1);
imshow(img);
title('Original Image');
subplot(2, 1, 2);
imshow(skippedImg);
title('Pixel Skipped Image');
