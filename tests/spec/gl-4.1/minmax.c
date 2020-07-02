/* Copyright © 2012 Intel Corporation
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice (including the next
 * paragraph) shall be included in all copies or substantial portions of the
 * Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

/** @file minmax.c
 *
 * Test for the minimum maximum values in section 6.2 "State Tables"
 * of the GL 4.1 spec.
 */

#include "piglit-util-gl.h"
#include "minmax-test.h"

PIGLIT_GL_TEST_CONFIG_BEGIN

	config.supports_gl_core_version = 41;
	config.supports_gl_compat_version = 41;

	config.window_visual = PIGLIT_GL_VISUAL_DOUBLE | PIGLIT_GL_VISUAL_RGBA;
	config.khr_no_error_support = PIGLIT_NO_ERRORS;

PIGLIT_GL_TEST_CONFIG_END

enum piglit_result
piglit_display(void)
{
	/* UNREACHED */
	return PIGLIT_FAIL;
}

void
piglit_init(int argc, char **argv)
{
	int vuniforms = 0, vblocks = 0;
	int tcuniforms = 0, tcblocks = 0;
	int teuniforms = 0, teblocks = 0;
	int guniforms = 0, gblocks = 0;
	int funiforms = 0, fblocks = 0;
	int blocksize = 0;

	piglit_print_minmax_header();

	/* These should be in the section with "Minimum Value" but
	 * appear in the section with "Initial Value".
	 */
	piglit_test_min_int(GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS, 64);
	piglit_test_min_int(GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS, 4);
	piglit_test_min_int(GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS, 4);
	piglit_test_min_int(GL_MAX_TRANSFORM_FEEDBACK_BUFFERS, 4);

	piglit_test_min_int(GL_MAX_CLIP_DISTANCES, 8);
	piglit_test_min_int(GL_SUBPIXEL_BITS, 4);
	piglit_test_min_int(GL_MAX_3D_TEXTURE_SIZE, 2048);
	piglit_test_min_int(GL_MAX_TEXTURE_SIZE, 16384);
	piglit_test_min_int(GL_MAX_ARRAY_TEXTURE_LAYERS, 2048);
	piglit_test_min_float(GL_MAX_TEXTURE_LOD_BIAS, 2.0);
	piglit_test_min_int(GL_MAX_CUBE_MAP_TEXTURE_SIZE, 16384);
	piglit_test_min_int(GL_MAX_RENDERBUFFER_SIZE, 16384);

	piglit_test_min_viewport_dimensions();

	piglit_test_min_int(GL_MAX_VIEWPORTS, 16);
	piglit_test_min_int(GL_VIEWPORT_SUBPIXEL_BITS, 0);
	piglit_test_range_float(GL_VIEWPORT_BOUNDS_RANGE, -32768, 32767);

	piglit_test_range_float(GL_POINT_SIZE_RANGE, 1, 1);
	piglit_test_range_float(GL_ALIASED_LINE_WIDTH_RANGE, 1, 1);
	piglit_test_range_float(GL_SMOOTH_LINE_WIDTH_RANGE, 1, 1);
	/* The spec lists 4, but the number should be 0, because hw drivers
	 * don't have to expose any non-core extensions like S3TC. */
	piglit_test_min_int(GL_NUM_COMPRESSED_TEXTURE_FORMATS, 0);
	piglit_test_min_int(GL_MAX_TEXTURE_BUFFER_SIZE, 65536);
	piglit_test_min_int(GL_MAX_RECTANGLE_TEXTURE_SIZE, 16384);

	piglit_test_tf_bits(GL_PRIMITIVES_GENERATED);
	piglit_test_tf_bits(GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN);
	piglit_test_oq_bits();

	piglit_test_min_int(GL_MAX_VERTEX_ATTRIBS, 16);
	piglit_test_min_int(GL_MAX_VERTEX_UNIFORM_COMPONENTS, 1024);
	piglit_test_min_int(GL_MAX_VERTEX_UNIFORM_BLOCKS, 12);
	piglit_test_min_int(GL_MAX_VERTEX_UNIFORM_VECTORS, 256);
	piglit_test_min_int(GL_MAX_VERTEX_OUTPUT_COMPONENTS, 64);
	piglit_test_min_int(GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS, 16);

	piglit_test_min_int(GL_MAX_TESS_GEN_LEVEL, 64);
	piglit_test_min_int(GL_MAX_PATCH_VERTICES, 32);
	piglit_test_min_int(GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS, 1024);
	piglit_test_min_int(GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS, 1024);
	piglit_test_min_int(GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS, 16);
	piglit_test_min_int(GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS, 16);
	piglit_test_min_int(GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS, 16);
	piglit_test_min_int(GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS, 128);
	piglit_test_min_int(GL_MAX_TESS_PATCH_COMPONENTS, 120);
	piglit_test_min_int(GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS, 4096);
	piglit_test_min_int(GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS, 128);
	piglit_test_min_int(GL_MAX_TESS_CONTROL_INPUT_COMPONENTS, 128);
	piglit_test_min_int(GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS, 128);
	piglit_test_min_int(GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS, 12);
	piglit_test_min_int(GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS, 12);
	/* MAX_GEOMETRY_UNIFORM_COMPONENTS was missing from the table
	 * from GL 3.2 through 4.1, though it's present in
	 * GL_ARB_geometry_shader and 4.2 with a value of 512.  Assume
	 * that it's an oversight in the spec.
	 */
	piglit_test_min_int(GL_MAX_GEOMETRY_UNIFORM_COMPONENTS, 512);
	piglit_test_min_int(GL_MAX_GEOMETRY_UNIFORM_BLOCKS, 12);
	piglit_test_min_int(GL_MAX_GEOMETRY_INPUT_COMPONENTS, 64);
	piglit_test_min_int(GL_MAX_GEOMETRY_OUTPUT_COMPONENTS, 128);
	piglit_test_min_int(GL_MAX_GEOMETRY_OUTPUT_VERTICES, 256);
	piglit_test_min_int(GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS, 1024);
	piglit_test_min_int(GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS, 16);
	piglit_test_min_int(GL_MAX_GEOMETRY_SHADER_INVOCATIONS, 32);
	piglit_test_min_int(GL_MAX_VERTEX_STREAMS, 4);

	piglit_test_min_int(GL_MAX_FRAGMENT_UNIFORM_COMPONENTS, 1024);
	piglit_test_min_int(GL_MAX_FRAGMENT_UNIFORM_BLOCKS, 12);
	piglit_test_min_int(GL_MAX_FRAGMENT_UNIFORM_VECTORS, 256);
	piglit_test_min_int(GL_MAX_FRAGMENT_INPUT_COMPONENTS, 128);
	piglit_test_min_int(GL_MAX_TEXTURE_IMAGE_UNITS, 16);
	piglit_test_max_int(GL_MIN_PROGRAM_TEXEL_OFFSET, -8);
	piglit_test_min_int(GL_MAX_PROGRAM_TEXEL_OFFSET, 7);
	piglit_test_max_int(GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET, -8);
	piglit_test_min_int(GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET, 7);

	piglit_test_min_int(GL_MAX_UNIFORM_BUFFER_BINDINGS, 60);
	piglit_test_min_int(GL_MAX_UNIFORM_BLOCK_SIZE, 16384);
	piglit_test_min_int(GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT, 1);
	piglit_test_min_int(GL_MAX_COMBINED_UNIFORM_BLOCKS, 60);

	glGetIntegerv(GL_MAX_VERTEX_UNIFORM_BLOCKS, &vblocks);
	glGetIntegerv(GL_MAX_VERTEX_UNIFORM_COMPONENTS, &vuniforms);
	glGetIntegerv(GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS, &tcblocks);
	glGetIntegerv(GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS, &tcuniforms);
	glGetIntegerv(GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS, &teblocks);
	glGetIntegerv(GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS, &teuniforms);
	glGetIntegerv(GL_MAX_GEOMETRY_UNIFORM_BLOCKS, &gblocks);
	glGetIntegerv(GL_MAX_GEOMETRY_UNIFORM_COMPONENTS, &guniforms);
	glGetIntegerv(GL_MAX_FRAGMENT_UNIFORM_BLOCKS, &fblocks);
	glGetIntegerv(GL_MAX_FRAGMENT_UNIFORM_COMPONENTS, &funiforms);
	glGetIntegerv(GL_MAX_UNIFORM_BLOCK_SIZE, &blocksize);

	piglit_test_min_int(GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS,
			    vblocks * blocksize / 4 + vuniforms);
	piglit_test_min_int(GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS,
			    fblocks * blocksize / 4 + funiforms);

	piglit_test_min_int(GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS,
			    tcblocks * blocksize / 4 + tcuniforms);
	piglit_test_min_int(GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS,
			    teblocks * blocksize / 4 + teuniforms);
	piglit_test_min_int(GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS,
			    gblocks * blocksize / 4 + guniforms);

	piglit_test_min_int(GL_MAX_VARYING_COMPONENTS, 60);
	piglit_test_min_int(GL_MAX_VARYING_VECTORS, 15);
	piglit_test_min_int(GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS, 80);

	piglit_test_min_int(GL_MAX_SUBROUTINES, 256);
	piglit_test_min_int(GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS, 1024);

	piglit_test_min_int(GL_MAX_SAMPLE_MASK_WORDS, 1);
	piglit_test_min_int(GL_MAX_COLOR_TEXTURE_SAMPLES, 1);
	piglit_test_min_int(GL_MAX_DEPTH_TEXTURE_SAMPLES, 1);
	piglit_test_min_int(GL_MAX_INTEGER_SAMPLES, 1);
	piglit_test_min_uint64(GL_MAX_SERVER_WAIT_TIMEOUT, 0);

	piglit_test_max_float(GL_MIN_FRAGMENT_INTERPOLATION_OFFSET, -0.5);
	piglit_test_min_float(GL_MAX_FRAGMENT_INTERPOLATION_OFFSET, 0.5);
	piglit_test_min_int(GL_FRAGMENT_INTERPOLATION_OFFSET_BITS, 4);
	piglit_test_min_int(GL_MAX_DRAW_BUFFERS, 8);
	piglit_test_min_int(GL_MAX_DUAL_SOURCE_DRAW_BUFFERS, 1);
	piglit_test_min_int(GL_SAMPLE_BUFFERS, 0);
	piglit_test_min_int(GL_SAMPLES, 0);
	piglit_test_min_int(GL_MAX_COLOR_ATTACHMENTS, 8);
	piglit_test_min_int(GL_MAX_SAMPLES, 4);

	if (!piglit_check_gl_error(GL_NO_ERROR))
		piglit_report_result(PIGLIT_FAIL);

	piglit_report_result(piglit_minmax_pass ? PIGLIT_PASS : PIGLIT_FAIL);
}
