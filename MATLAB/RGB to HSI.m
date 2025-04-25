function rgb_to_hsi_demo()
    RGB = imread('Enter your image path here'); 
    HSI = rgb2hsi(RGB);
    figure('Position', [100, 100, 1200, 800]);
    subplot(2, 3, 1);
    imshow(RGB, 'InitialMagnification', 'fit'); 
    title('Original RGB Image', 'FontSize', 12);
    subplot(2, 3, 2), imshow(HSI(:,:,1), 'InitialMagnification', 'fit'), title('Hue', 'FontSize', 12);
    subplot(2, 3, 3), imshow(HSI(:,:,2), 'InitialMagnification', 'fit'), title('Saturation', 'FontSize', 12);
    subplot(2, 3, 4), imshow(HSI(:,:,3), 'InitialMagnification', 'fit'), title('Intensity', 'FontSize', 12);
    combined_hsi = im2uint8(HSI); 
    subplot(2, 3, 5), imshow(combined_hsi, 'InitialMagnification', 'fit'), title('Combined HSI', 'FontSize', 12);
    subplot(2, 3, 6), axis off; 
end
function HSI = rgb2hsi(RGB)
    RGB = double(RGB) / 255;
    R = RGB(:,:,1);
    G = RGB(:,:,2);
    B = RGB(:,:,3);
    I = (R + G + B) / 3;
    num = min(R, min(G, B));
    den = I + eps; 
    S = 1 - (num ./ den); % S = 1 - (min(R,G,B) / I)
    denom = sqrt((R - G).^2 + (R - B) .* (G - B) + eps);
    theta = acos(0.5 * ((R - G) + (R - B)) ./ denom); 
    H = zeros(size(I)); % Initialize Hue matrix
    H(B <= G) = theta(B <= G);               
    H(B > G) = 2 * pi - theta(B > G);      
    H = H / (2 * pi);
    HSI = cat(3, H, S, I);
end
