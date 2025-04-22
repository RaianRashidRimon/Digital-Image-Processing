function rgb_channels_demo()
    RGB = imread('Enter your image path here'); 
    R = RGB(:,:,1); % Red channel
    G = RGB(:,:,2); % Green channel
    B = RGB(:,:,3); % Blue channel
    zero_channel = zeros(size(R), 'uint8');
    RedChannelImage = cat(3, R, zero_channel, zero_channel); % Red channel in color
    GreenChannelImage = cat(3, zero_channel, G, zero_channel); % Green channel in color
    BlueChannelImage = cat(3, zero_channel, zero_channel, B); % Blue channel in color
    figure;
    subplot(2, 2, 1);
    imshow(RGB);
    title('Original RGB Image', 'FontSize', 12);
    subplot(2, 2, 2);
    imshow(RedChannelImage);
    title('Red Channel', 'FontSize', 12);
    subplot(2, 2, 3);
    imshow(GreenChannelImage);
    title('Green Channel', 'FontSize', 12);
    subplot(2, 2, 4);
    imshow(BlueChannelImage);
    title('Blue Channel', 'FontSize', 12);
end
