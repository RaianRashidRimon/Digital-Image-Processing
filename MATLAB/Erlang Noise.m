originalImage = imread('Enter your image path here');
originalImage = im2double(originalImage);

% Add Erlang noise (Gamma distribution with integer shape)
erlangShape = 2;      % k
erlangScale = 0.2;    % theta
erlangNoiseImage = originalImage;

for i = 1:size(originalImage, 3)
    erlangNoise = gamrnd(erlangShape, erlangScale, size(originalImage, 1), size(originalImage, 2));
    erlangNoiseImage(:, :, i) = originalImage(:, :, i) + erlangNoise;
end

% Clip values to [0, 1] range
erlangNoiseImage = min(max(erlangNoiseImage, 0), 1);

% Display original and noisy images
figure;
subplot(1,2,1);
imshow(originalImage);
title('Original Image');

subplot(1,2,2);
imshow(erlangNoiseImage);
title('Image with Erlang (Gamma) Noise');
