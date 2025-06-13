#extension GL_EXT_texture_array : enable  
uniform vec4 arrayDepth;  
  
layout (local_size_x = 1, local_size_y = 1) in;  
void main()  
{  
	uint workGroupId = gl_WorkGroupID.x;  
	uint texWidth = uint(uTD2DInfos[0].res.z);  
	uint texHeight = uint(uTD2DInfos[0].res.w);  
	uint texSize = texWidth * texHeight;  
	float blockSize = texSize / arrayDepth.s;  
  
	for (uint i = int(ceil(workGroupId * blockSize)); i < int(ceil((workGroupId + 1) * blockSize)); i++) {  
			ivec2 uv = ivec2(i % texWidth, i / texWidth);  
  
			vec4 position = texelFetch(sTD2DInputs[0], uv, 0);  
			ivec3 voxelCoords = ivec3(int(position.x + 13), int(position.y + 20), int(position.z + 13));  
			if (voxelCoords.x < 0 || voxelCoords.x >= 26 || voxelCoords.y < 0 || voxelCoords.y >= 40 || voxelCoords.z < 0 || voxelCoords.z >= 26) {  
				continue; // Skip out-of-bounds coordinates  
			}  
  
			vec4 existingColor = imageLoad(mTDComputeOutputs[0], ivec3(voxelCoords.x, voxelCoords.y * 26 + voxelCoords.z, workGroupId));  
			vec4 incomingColor = texelFetch(sTD2DInputs[1], uv, 0);  
			imageStore(mTDComputeOutputs[0], ivec3(voxelCoords.x, voxelCoords.y * 26 + voxelCoords.z, workGroupId), existingColor + incomingColor * position.w);  
	}  
  
}  
