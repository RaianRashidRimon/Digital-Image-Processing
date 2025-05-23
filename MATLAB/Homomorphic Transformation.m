originalImage = imread('Enter your image path here');
grayImage = rgb2gray(originalImage);
grayImage = double(grayImage);
noiseLevel = 50;
noisyImage = grayImage + noiseLevel * randn(size(grayImage));
logImage = log(1 + noisyImage);
fftImage = fft2(logImage);
fftImageShifted = fftshift(fftImage);
[rows, cols] = size(fftImageShifted);
[x, y] = meshgrid(1:cols, 1:rows);
centerX = cols / 2;
centerY = rows / 2;
sigma = 1;
highPassFilter = 1 - exp(-((x - centerX).^2 + (y - centerY).^2) / (2 * sigma^2));
filteredFFT = fftImageShifted .* highPassFilter;
filteredImage = ifft2(ifftshift(filteredFFT));
outputImage = exp(real(filteredImage)) - 1;
noisyImage = mat2gray(noisyImage);
outputImage = mat2gray(outputImage);
figure;
subplot(1, 3, 1);
imshow(grayImage, []);
title('Original Grayscale Image');
subplot(1, 3, 2);
imshow(noisyImage, []);
title('Noisy Image');
subplot(1, 3, 3);
imshow(outputImage, []);
title('Homomorphic Filtered Image');
