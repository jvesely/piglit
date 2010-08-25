/* PASS */
#version 110

uniform float u_float;
uniform vec2 u_vec2;
uniform vec3 u_vec3;
uniform vec4 u_vec4;
uniform ivec2 u_ivec2;
uniform ivec3 u_ivec3;
uniform ivec4 u_ivec4;
uniform bvec2 u_bvec2;
uniform bvec3 u_bvec3;
uniform bvec4 u_bvec4;
uniform mat2 u_mat2;
uniform mat3 u_mat3;
uniform mat4 u_mat4;

void main()
{
  gl_Position = gl_Vertex;

  float t_float = float(0.0);
  bool t_bool = false;
  vec2  t_vec2  = vec2 (0.0);
  bvec2 t_bvec2 = bvec2(0.0);
  mat2  t_mat2  = mat2 (0.0);
  vec3  t_vec3  = vec3 (0.0);
  bvec3 t_bvec3 = bvec3(0.0);
  mat3  t_mat3  = mat3 (0.0);
  vec4  t_vec4  = vec4 (0.0);
  bvec4 t_bvec4 = bvec4(0.0);
  mat4  t_mat4  = mat4 (0.0);

  t_float += radians(u_float);
  t_vec2 += radians(u_vec2);
  t_vec3 += radians(u_vec3);
  t_vec4 += radians(u_vec4);
  t_float += degrees(u_float);
  t_vec2 += degrees(u_vec2);
  t_vec3 += degrees(u_vec3);
  t_vec4 += degrees(u_vec4);
  t_float += sin(u_float);
  t_vec2 += sin(u_vec2);
  t_vec3 += sin(u_vec3);
  t_vec4 += sin(u_vec4);
  t_float += cos(u_float);
  t_vec2 += cos(u_vec2);
  t_vec3 += cos(u_vec3);
  t_vec4 += cos(u_vec4);
  t_float += tan(u_float);
  t_vec2 += tan(u_vec2);
  t_vec3 += tan(u_vec3);
  t_vec4 += tan(u_vec4);
  t_float += asin(u_float);
  t_vec2 += asin(u_vec2);
  t_vec3 += asin(u_vec3);
  t_vec4 += asin(u_vec4);
  t_float += acos(u_float);
  t_vec2 += acos(u_vec2);
  t_vec3 += acos(u_vec3);
  t_vec4 += acos(u_vec4);
  t_float += atan(u_float);
  t_vec2 += atan(u_vec2);
  t_vec3 += atan(u_vec3);
  t_vec4 += atan(u_vec4);
  t_float += exp(u_float);
  t_vec2 += exp(u_vec2);
  t_vec3 += exp(u_vec3);
  t_vec4 += exp(u_vec4);
  t_float += log(u_float);
  t_vec2 += log(u_vec2);
  t_vec3 += log(u_vec3);
  t_vec4 += log(u_vec4);
  t_float += exp2(u_float);
  t_vec2 += exp2(u_vec2);
  t_vec3 += exp2(u_vec3);
  t_vec4 += exp2(u_vec4);
  t_float += log2(u_float);
  t_vec2 += log2(u_vec2);
  t_vec3 += log2(u_vec3);
  t_vec4 += log2(u_vec4);
  t_float += sqrt(u_float);
  t_vec2 += sqrt(u_vec2);
  t_vec3 += sqrt(u_vec3);
  t_vec4 += sqrt(u_vec4);
  t_float += inversesqrt(u_float);
  t_vec2 += inversesqrt(u_vec2);
  t_vec3 += inversesqrt(u_vec3);
  t_vec4 += inversesqrt(u_vec4);
  t_float += abs(u_float);
  t_vec2 += abs(u_vec2);
  t_vec3 += abs(u_vec3);
  t_vec4 += abs(u_vec4);
  t_float += sign(u_float);
  t_vec2 += sign(u_vec2);
  t_vec3 += sign(u_vec3);
  t_vec4 += sign(u_vec4);
  t_float += floor(u_float);
  t_vec2 += floor(u_vec2);
  t_vec3 += floor(u_vec3);
  t_vec4 += floor(u_vec4);
  t_float += ceil(u_float);
  t_vec2 += ceil(u_vec2);
  t_vec3 += ceil(u_vec3);
  t_vec4 += ceil(u_vec4);
  t_float += fract(u_float);
  t_vec2 += fract(u_vec2);
  t_vec3 += fract(u_vec3);
  t_vec4 += fract(u_vec4);
  t_float += length(u_float);
  t_vec2 += length(u_vec2);
  t_vec3 += length(u_vec3);
  t_vec4 += length(u_vec4);
  t_float += normalize(u_float);
  t_vec2 += normalize(u_vec2);
  t_vec3 += normalize(u_vec3);
  t_vec4 += normalize(u_vec4);
  t_float += dFdx(u_float);
  t_vec2 += dFdx(u_vec2);
  t_vec3 += dFdx(u_vec3);
  t_vec4 += dFdx(u_vec4);
  t_float += dFdy(u_float);
  t_vec2 += dFdy(u_vec2);
  t_vec3 += dFdy(u_vec3);
  t_vec4 += dFdy(u_vec4);
  t_float += fwidth(u_float);
  t_vec2 += fwidth(u_vec2);
  t_vec3 += fwidth(u_vec3);
  t_vec4 += fwidth(u_vec4);

  t_float += atan(u_float, -u_float);
  t_vec2 += atan(u_vec2, -u_vec2);
  t_vec3 += atan(u_vec3, -u_vec3);
  t_vec4 += atan(u_vec4, -u_vec4);
  t_float += pow(u_float, -u_float);
  t_vec2 += pow(u_vec2, -u_vec2);
  t_vec3 += pow(u_vec3, -u_vec3);
  t_vec4 += pow(u_vec4, -u_vec4);
  t_float += mod(u_float, -u_float);
  t_vec2 += mod(u_vec2, -u_vec2);
  t_vec3 += mod(u_vec3, -u_vec3);
  t_vec4 += mod(u_vec4, -u_vec4);
  t_float += min(u_float, -u_float);
  t_vec2 += min(u_vec2, -u_vec2);
  t_vec3 += min(u_vec3, -u_vec3);
  t_vec4 += min(u_vec4, -u_vec4);
  t_float += max(u_float, -u_float);
  t_vec2 += max(u_vec2, -u_vec2);
  t_vec3 += max(u_vec3, -u_vec3);
  t_vec4 += max(u_vec4, -u_vec4);
  t_float += step(u_float, -u_float);
  t_vec2 += step(u_vec2, -u_vec2);
  t_vec3 += step(u_vec3, -u_vec3);
  t_vec4 += step(u_vec4, -u_vec4);
  t_float += distance(u_float, -u_float);
  t_vec2 += distance(u_vec2, -u_vec2);
  t_vec3 += distance(u_vec3, -u_vec3);
  t_vec4 += distance(u_vec4, -u_vec4);
  t_float += dot(u_float, -u_float);
  t_vec2 += dot(u_vec2, -u_vec2);
  t_vec3 += dot(u_vec3, -u_vec3);
  t_vec4 += dot(u_vec4, -u_vec4);
  t_float += reflect(u_float, -u_float);
  t_vec2 += reflect(u_vec2, -u_vec2);
  t_vec3 += reflect(u_vec3, -u_vec3);
  t_vec4 += reflect(u_vec4, -u_vec4);

  t_float += clamp(u_float, -u_float, 11.7 * u_float);
  t_vec2 += clamp(u_vec2, -u_vec2, 11.7 * u_vec2);
  t_vec3 += clamp(u_vec3, -u_vec3, 11.7 * u_vec3);
  t_vec4 += clamp(u_vec4, -u_vec4, 11.7 * u_vec4);
  t_float += mix(u_float, -u_float, 11.7 * u_float);
  t_vec2 += mix(u_vec2, -u_vec2, 11.7 * u_vec2);
  t_vec3 += mix(u_vec3, -u_vec3, 11.7 * u_vec3);
  t_vec4 += mix(u_vec4, -u_vec4, 11.7 * u_vec4);
  t_float += smoothstep(u_float, -u_float, 11.7 * u_float);
  t_vec2 += smoothstep(u_vec2, -u_vec2, 11.7 * u_vec2);
  t_vec3 += smoothstep(u_vec3, -u_vec3, 11.7 * u_vec3);
  t_vec4 += smoothstep(u_vec4, -u_vec4, 11.7 * u_vec4);
  t_float += faceforward(u_float, -u_float, 11.7 * u_float);
  t_vec2 += faceforward(u_vec2, -u_vec2, 11.7 * u_vec2);
  t_vec3 += faceforward(u_vec3, -u_vec3, 11.7 * u_vec3);
  t_vec4 += faceforward(u_vec4, -u_vec4, 11.7 * u_vec4);

  t_float = mod(u_float, u_float);
  t_vec2 = mod(u_vec2, u_float);
  t_vec3 = mod(u_vec3, u_float);
  t_vec4 = mod(u_vec4, u_float);
  t_float = min(u_float, u_float);
  t_vec2 = min(u_vec2, u_float);
  t_vec3 = min(u_vec3, u_float);
  t_vec4 = min(u_vec4, u_float);
  t_float = max(u_float, u_float);
  t_vec2 = max(u_vec2, u_float);
  t_vec3 = max(u_vec3, u_float);
  t_vec4 = max(u_vec4, u_float);
  t_float = clamp(u_float, u_float, u_float);
  t_vec2 = clamp(u_vec2, u_float, u_float);
  t_vec3 = clamp(u_vec3, u_float, u_float);
  t_vec4 = clamp(u_vec4, u_float, u_float);
  t_float = mix(u_float, u_float, u_float);
  t_vec2 = mix(u_vec2, u_vec2, u_float);
  t_vec3 = mix(u_vec3, u_vec3, u_float);
  t_vec4 = mix(u_vec4, u_vec4, u_float);
  t_float = step(u_float, u_float);
  t_vec2 = step(u_float, u_vec2);
  t_vec3 = step(u_float, u_vec3);
  t_vec4 = step(u_float, u_vec4);
  t_float = smoothstep(u_float, u_float, u_float);
  t_vec2 = smoothstep(u_float, u_float, u_vec2);
  t_vec3 = smoothstep(u_float, u_float, u_vec3);
  t_vec4 = smoothstep(u_float, u_float, u_vec4);
  t_float = refract(u_float, u_float, u_float);
  t_vec2 = refract(u_vec2, u_vec2, u_float);
  t_vec3 = refract(u_vec3, u_vec3, u_float);
  t_vec4 = refract(u_vec4, u_vec4, u_float);
  t_float = noise1(u_float);
  t_float = noise1(u_vec2);
  t_float = noise1(u_vec3);
  t_float = noise1(u_vec4);
  t_vec2 = noise2(u_float);
  t_vec2 = noise2(u_vec2);
  t_vec2 = noise2(u_vec3);
  t_vec2 = noise2(u_vec4);
  t_vec3 = noise3(u_float);
  t_vec3 = noise3(u_vec2);
  t_vec3 = noise3(u_vec3);
  t_vec3 = noise3(u_vec4);
  t_vec4 = noise4(u_float);
  t_vec4 = noise4(u_vec2);
  t_vec4 = noise4(u_vec3);
  t_vec4 = noise4(u_vec4);

  t_bvec2 = lessThan(u_vec2, u_vec2);
  t_bvec3 = lessThan(u_vec3, u_vec3);
  t_bvec4 = lessThan(u_vec4, u_vec4);
  t_bvec2 = lessThan(u_ivec2, u_ivec2);
  t_bvec3 = lessThan(u_ivec3, u_ivec3);
  t_bvec4 = lessThan(u_ivec4, u_ivec4);
  t_bvec2 = lessThanEqual(u_vec2, u_vec2);
  t_bvec3 = lessThanEqual(u_vec3, u_vec3);
  t_bvec4 = lessThanEqual(u_vec4, u_vec4);
  t_bvec2 = lessThanEqual(u_ivec2, u_ivec2);
  t_bvec3 = lessThanEqual(u_ivec3, u_ivec3);
  t_bvec4 = lessThanEqual(u_ivec4, u_ivec4);
  t_bvec2 = greaterThan(u_vec2, u_vec2);
  t_bvec3 = greaterThan(u_vec3, u_vec3);
  t_bvec4 = greaterThan(u_vec4, u_vec4);
  t_bvec2 = greaterThan(u_ivec2, u_ivec2);
  t_bvec3 = greaterThan(u_ivec3, u_ivec3);
  t_bvec4 = greaterThan(u_ivec4, u_ivec4);
  t_bvec2 = greaterThanEqual(u_vec2, u_vec2);
  t_bvec3 = greaterThanEqual(u_vec3, u_vec3);
  t_bvec4 = greaterThanEqual(u_vec4, u_vec4);
  t_bvec2 = greaterThanEqual(u_ivec2, u_ivec2);
  t_bvec3 = greaterThanEqual(u_ivec3, u_ivec3);
  t_bvec4 = greaterThanEqual(u_ivec4, u_ivec4);
  t_bvec2 = equal(u_vec2, u_vec2);
  t_bvec3 = equal(u_vec3, u_vec3);
  t_bvec4 = equal(u_vec4, u_vec4);
  t_bvec2 = equal(u_ivec2, u_ivec2);
  t_bvec3 = equal(u_ivec3, u_ivec3);
  t_bvec4 = equal(u_ivec4, u_ivec4);
  t_bvec2 = notEqual(u_vec2, u_vec2);
  t_bvec3 = notEqual(u_vec3, u_vec3);
  t_bvec4 = notEqual(u_vec4, u_vec4);
  t_bvec2 = notEqual(u_ivec2, u_ivec2);
  t_bvec3 = notEqual(u_ivec3, u_ivec3);
  t_bvec4 = notEqual(u_ivec4, u_ivec4);

  t_bvec2 = equal(u_bvec2, u_bvec2);
  t_bvec3 = equal(u_bvec3, u_bvec3);
  t_bvec4 = equal(u_bvec4, u_bvec4);
  t_bvec2 = notEqual(u_bvec2, u_bvec2);
  t_bvec3 = notEqual(u_bvec3, u_bvec3);
  t_bvec4 = notEqual(u_bvec4, u_bvec4);
  t_bool = any(u_bvec2);
  t_bool = any(u_bvec3);
  t_bool = any(u_bvec4);
  t_bool = all(u_bvec2);
  t_bool = all(u_bvec3);
  t_bool = all(u_bvec4);
  t_bvec2 = not(u_bvec2);
  t_bvec3 = not(u_bvec3);
  t_bvec4 = not(u_bvec4);

  t_mat2 = matrixCompMult(u_mat2, u_mat2);
  t_mat3 = matrixCompMult(u_mat3, u_mat3);
  t_mat4 = matrixCompMult(u_mat4, u_mat4);
}
