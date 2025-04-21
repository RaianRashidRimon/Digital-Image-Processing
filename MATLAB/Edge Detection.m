function show_all_edge_detections(input_image)
    rgb_img = im2double(imread('Enter your image path here'));
    if size(rgb_img, 3) == 3
        gray_img = rgb2gray(rgb_img);
    else
        gray_img = rgb_img;
    end
    
    sobel_edge = sobel_detection(gray_img);
    prewitt_edge = prewitt_detection(gray_img);
    isotropic_edge = isotropic_detection(gray_img);
    roberts_edge = roberts_detection(gray_img);
    
    figure;
    subplot(2, 3, 1), imshow(rgb_img), title('Original RGB Image');
    subplot(2, 3, 2), imshow(gray_img), title('Grayscale Image');
    subplot(2, 3, 3), imshow(sobel_edge, []), title('Sobel Edge Detection');
    subplot(2, 3, 4), imshow(prewitt_edge, []), title('Prewitt Edge Detection');
    subplot(2, 3, 5), imshow(isotropic_edge, []), title('Isotropic Edge Detection');
    subplot(2, 3, 6), imshow(roberts_edge, []), title('Roberts Edge Detection');
end

function edge_image = sobel_detection(img)
    sobel_x = [-1 0 1; -2 0 2; -1 0 1];
    sobel_y = [1 2 1; 0 0 0; -1 -2 -1];
    grad_x = conv2(img, sobel_x, 'same');
    grad_y = conv2(img, sobel_y, 'same');
    edge_image = sqrt(grad_x.^2 + grad_y.^2);
end

function edge_image = prewitt_detection(img)
    prewitt_x = [-1 0 1; -1 0 1; -1 0 1];
    prewitt_y = [1 1 1; 0 0 0; -1 -1 -1];
    grad_x = conv2(img, prewitt_x, 'same');
    grad_y = conv2(img, prewitt_y, 'same');
    edge_image = sqrt(grad_x.^2 + grad_y.^2);
end

function edge_image = isotropic_detection(img)
    sigma = 1;
    gauss_filter = fspecial('gaussian', 5, sigma);
    smoothed_img = conv2(img, gauss_filter, 'same');
    laplacian_filter = fspecial('laplacian', 0);
    edge_image = conv2(smoothed_img, laplacian_filter, 'same');
    edge_image = abs(edge_image);
end

function edge_image = roberts_detection(img)
    roberts_x = [1 0; 0 -1];
    roberts_y = [0 1; -1 0];
    grad_x = conv2(img, roberts_x, 'same');
    grad_y = conv2(img, roberts_y, 'same');
    edge_image = sqrt(grad_x.^2 + grad_y.^2);
end
