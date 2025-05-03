originalImage = imread('Enter your image path here');
originalImage = im2double(originalImage);

% Add Rayleigh noise
rayleighScale = 0.5;
rayleighNoiseImage = originalImage;

for i = 1:size(originalImage, 3)
    rayleighNoise = raylrnd(rayleighScale, size(originalImage, 1), size(originalImage, 2));
    rayleighNoiseImage(:, :, i) = originalImage(:, :, i) + rayleighNoise;
end

% Clip values to [0, 1] range
rayleighNoiseImage = min(max(rayleighNoiseImage, 0), 1);

% Display original and noisy images
figure;
subplot(1,2,1);
imshow(originalImage);
title('Original Image');

subplot(1,2,2);
imshow(rayleighNoiseImage);
title('Image with Rayleigh Noise');