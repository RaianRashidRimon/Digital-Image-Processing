kernelSize = 3;  
laplacianKernel = -4 * ones(kernelSize) + eye(kernelSize) * (kernelSize^2 - 1);
inputImage = imread('Enter the path to the image here');
if size(inputImage, 3) == 3
    inputImage = rgb2gray(inputImage);
end
filteredImage = conv2(double(inputImage), laplacianKernel, 'same');
filteredImage = mat2gray(filteredImage);
figure('Position', [100, 100, 600, 800]);
subplot(2, 1, 1);
imshow(inputImage);
title('Original Image');
subplot(2, 1, 2);
imshow(filteredImage);
title('Laplacian Filtered Image');
