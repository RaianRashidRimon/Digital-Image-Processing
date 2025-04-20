img = imread('Enter your image path here');
newRows = 500; 
newCols = 500; 
[originalRows, originalCols, numChannels] = size(img);
resizedImg = uint8(zeros(newRows, newCols, numChannels));
rowScale = originalRows / newRows;
colScale = originalCols / newCols;
for r = 1:newRows
    for c = 1:newCols
        origRow = round((r - 0.5) * rowScale + 0.5);
        origCol = round((c - 0.5) * colScale + 0.5);
        origRow = max(1, min(originalRows, origRow));
        origCol = max(1, min(originalCols, origCol));
        resizedImg(r, c, :) = img(origRow, origCol, :); 
    end
end
figure('Position', [100, 100, 600, 800]);
subplot(2, 1, 1);
imshow(img);
title('Original Image');
subplot(2, 1, 2);
imshow(resizedImg);
title('Resized Image using Replication Method');
