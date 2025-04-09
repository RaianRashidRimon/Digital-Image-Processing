inputImage = imread('Enter the path to the image here'); 


figure;
subplot(2, 2, 1);
imshow(inputImage);
title('Original Image');

if size(inputImage, 3) == 3
    grayImage = rgb2gray(inputImage);
else
    grayImage = inputImage;
end

minIntensity = double(min(grayImage(:)));
maxIntensity = double(max(grayImage(:)));

newMin = minIntensity + 0.1 * (maxIntensity - minIntensity);
newMax = maxIntensity - 0.1 * (maxIntensity - minIntensity);

stretchedImage = imadjust(grayImage, [newMin/255; newMax/255], [0; 1]);

subplot(2, 2, 3);
imshow(stretchedImage);
title('Contrast-Stretched Image');

disp(['Original min: ', num2str(minIntensity)]);
disp(['Original max: ', num2str(maxIntensity)]);
disp(['New min: ', num2str(newMin)]);
disp(['New max: ', num2str(newMax)]);
