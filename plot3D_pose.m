function [] = plot3D_pose(pose_data, connections)

for i = 1:size(pose_data, 2)
    scatter3(pose_data(1, i), pose_data(2, i), pose_data(3, i), 'r', 'filled')
end

for i = 1:size(connections, 1)
    plot3(pose_data(1, connections(i, :)), pose_data(2, connections(i, :)), pose_data(3, connections(i, :)), ...
        'Color', 'b', 'LineWidth', 3);
end

end