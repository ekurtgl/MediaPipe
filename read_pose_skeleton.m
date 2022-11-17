clc; clear; close all;

datapath = '/mnt/HDD04/WASL Dataset/Scripts/pose_skeletons/';
savepath = '/mnt/HDD04/WASL Dataset/Scripts/pose_skeletons_mat/';
folders = dir(datapath);
folders = folders(3:end);

for f = 5:length(folders)
    tic
    disp(['Processing ' int2str(f) '/' int2str(length(folders))]);
    files = dir([folders(f).folder '/' folders(f).name '/*txt']);
    pose = zeros(33, 3, length(files));
    for i = 31:length(files)
        figure(1);
        clf;
        hold on; 

        fid = fopen([files(i).folder '/' files(i).name]);
        content = cell(1);
        content{1} = fgetl(fid);
        cnt = 2;
        while ischar(content{cnt-1})
            content{cnt} = fgetl(fid);
            cnt = cnt + 1;
        end
        fclose(fid);

        if isempty(content)
            continue
        end
        content = content(1:end-1);
        [pose_data, connections] = get_pose_data(content);
        pose(:, :, i) = pose_data.';
        
        plot3D_pose(pose_data, connections);
    end
    save([savepath folders(f).name '.mat'], 'hands');
    toc
end




