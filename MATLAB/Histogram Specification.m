
inputImage = imread('Enter the path to the image here');
referenceImage = imread('Enter the path to the reference image here'); 
if size(inputImage, 3) == 3
    inputGray = rgb2gray(inputImage);
else
    inputGray = inputImage;
end

if size(referenceImage, 3) == 3
    referenceGray = rgb2gray(referenceImage);
else
    referenceGray = referenceImage;
end
[inputCounts, inputGrayLevels] = imhist(inputGray);
[referenceCounts, referenceGrayLevels] = imhist(referenceGray);

inputCDF = cumsum(inputCounts) / numel(inputGray);
referenceCDF = cumsum(referenceCounts) / numel(referenceGray);
mapping = zeros(256, 1, 'uint8');
cdfMap = zeros(256, 1);

for i = 1:256
    [~, idx] = min(abs(inputCDF(i) - referenceCDF));
    mapping(i) = referenceGrayLevels(idx);
end

specifiedImage = mapping(double(inputGray) + 1);
[specifiedCounts, specifiedGrayLevels] = imhist(specifiedImage);
figure;
subplot(2,2,1);
imshow(inputGray);
title('Original Grayscale Image');

subplot(2,2,2);
bar(inputGrayLevels, inputCounts, 'BarWidth', 1);
title('Histogram of Original Image');
xlabel('Gray Level');
ylabel('Frequency');
subplot(2,2,3);
imshow(referenceGray);
title('Reference Grayscale Image');

subplot(2,2,4);
bar(referenceGrayLevels, referenceCounts, 'BarWidth', 1);
title('Histogram of Reference Image');
xlabel('Gray Level');
ylabel('Frequency');
figure;

subplot(2,2,1);
imshow(specifiedImage, []);
title('Histogram Specified Image');

subplot(2,2,2);
bar(specifiedGrayLevels, specifiedCounts, 'BarWidth', 1);
title('Histogram of Specified Image');
xlabel('Gray Level');
ylabel('Frequency');