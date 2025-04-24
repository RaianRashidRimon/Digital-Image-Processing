function rgb_to_grayscale_demo()
    RGB = imread('Enter your image path here'); 
    grayscaleImage = rgb2gray(RGB);
    figure;
    subplot(1, 2, 1);
    imshow(RGB);
    title('Original RGB Image', 'FontSize', 12);
    subplot(1, 2, 2);
    imshow(grayscaleImage);
    title('Grayscale Image', 'FontSize', 12);
end
