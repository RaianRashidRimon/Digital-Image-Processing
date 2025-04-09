
    img = imread('Enter the path to the image here');
    img = im2double(img)
    negativee = 1 - img
        negative_img = 255 - img;
  
    figure;
    subplot(1, 2, 1);
    imshow(img);
    title('Original Image');
    
    subplot(1, 2, 2);
    imshow(negativee);
    title('Negative Image')
