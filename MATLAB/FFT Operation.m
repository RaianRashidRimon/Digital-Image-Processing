originalImage = imread('Enter your image path here');
if size(originalImage, 3) == 3
    grayImage = rgb2gray(originalImage);
else
    grayImage = originalImage;
end
grayImage = double(grayImage);
fftImage = fft2(grayImage);
fftImageShifted = fftshift(fftImage);
magnitudeSpectrum = abs(fftImageShifted);
magnitudeSpectrum = log(1 + magnitudeSpectrum);
magnitudeSpectrum = mat2gray(magnitudeSpectrum);
figure;
subplot(1, 2, 1);
imshow(grayImage, []);
title('Original Grayscale Image');
subplot(1, 2, 2);
imshow(magnitudeSpectrum, []);
title('Magnitude Spectrum');