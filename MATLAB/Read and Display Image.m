% Prompt user to select an image file
[filename, pathname] = uigetfile({'*.jpg;*.png;*.bmp;*.tiff', 'Image Files (*.jpg, *.png, *.bmp, *.tiff)'}, 'Select an Image File');
 
% Check if the user canceled the file selection
if isequal(filename, 0)
    disp('User canceled the file selection.');
else
    % Construct the full file path
    fullPath = fullfile(pathname, filename);
    
    % Read the image from the file
    img = imread(fullPath);
    
    % Display the image
    figure; % Open a new figure window
    imshow(img);
    
    % Optionally, add a title to the image window
    title('Displayed Image');
end

