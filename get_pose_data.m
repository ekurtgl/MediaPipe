function [pose_data, connections] = get_pose_data(content)

connections = [0, 1;
               1, 2;
               2, 3;
               3, 7;
               0, 4;
               4, 5;
               5, 6;
               6, 8;
               9, 10;
               11, 12;
               11, 13;
               13, 15;
               15, 17;
               15, 21;
               15, 19;
               17, 19;
               12, 14;
               14, 16;
               16, 18;
               16, 22;
               16, 20;
               18, 20;
               11, 23;
               23, 25;
               25, 27;
               27, 29;
               27, 31;
               29, 31;
               12, 24;
               23, 24;
               24, 26;
               26, 28;
               28, 30;
               28, 32;
               30, 32] + 1;
           
num_mark = 33;
pose_data = zeros(3, num_mark);

for i = 1:3
    c = strsplit(content{i});
    c = c(1:end-1);
    c = cellfun(@str2num, c);
    
    if mod(i, 3) == 1
        pose_data(1,:) = c;
    elseif mod(i, 3) == 2
        pose_data(2,:) = c;
    elseif mod(i, 3) == 0
        pose_data(3,:) = c;
    end
end


end