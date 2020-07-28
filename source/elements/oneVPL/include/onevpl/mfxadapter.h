/*############################################################################
  # Copyright (C) 2019-2020 Intel Corporation
  #
  # SPDX-License-Identifier: MIT
  ############################################################################*/

#include "mfxdefs.h"
#if (MFX_VERSION >= 1031)
#ifndef __MFXADAPTER_H__
#define __MFXADAPTER_H__

#include "mfxstructures.h"

#ifdef __cplusplus
extern "C"
{
#endif

/*!
   @brief
    This function returns a list of adapters that are suitable to handle workload input_info. The list is sorted in priority order, with iGPU given the highest precedence.
    This rule may change in the future. If input_info pointer is NULL, the list of all available adapters will be returned.

   @param[in] input_info Pointer to workload description. See mfxComponentInfo description for details.
   @param[out] adapters  Pointer to output description of all suitable adapters for input workload. See mfxAdaptersInfo description for details.

   @return
   MFX_ERR_NONE The function completed successfully. \n
   MFX_ERR_NULL_PTR  input_info or adapters pointer is NULL. \n
   MFX_ERR_NOT_FOUND  No suitable adapters found. \n
   MFX_WRN_OUT_OF_RANGE  Not enough memory to report back entire list of adapters. In this case as many adapters as possible will be returned.
*/
mfxStatus MFX_CDECL MFXQueryAdapters(mfxComponentInfo* input_info, mfxAdaptersInfo* adapters);

/*!
   @brief
    This function returns list of adapters that are suitable to decode input bitstream. The list is sorted in priority order, with iGPU given the highest precedence. This rule may change in the  . This function is a simplification of MFXQueryAdapters, because bitstream is a description of the workload itself.

   @param[in]  bitstream Pointer to bitstream with input data.
   @param[in]  codec_id  Codec ID to determine the type of codec for the input bitstream.
   @param[out] adapters  Pointer to the output list of adapters. Memory should be allocated by user. See mfxAdaptersInfo description for details.

   @return
   MFX_ERR_NONE The function completed successfully. \n
   MFX_ERR_NULL_PTR  bitstream or adapters pointer is NULL. \n
   MFX_ERR_NOT_FOUND No suitable adapters found. \n
   MFX_WRN_OUT_OF_RANGE Not enough memory to report back entire list of adapters. In this case as many adapters as possible will be returned.
*/
mfxStatus MFX_CDECL MFXQueryAdaptersDecode(mfxBitstream* bitstream, mfxU32 codec_id, mfxAdaptersInfo* adapters);

/*!
   @brief
    This function returns the number of detected graphics adapters. It can be used before calling MFXQueryAdapters  to determine the size of input data that the user will need to allocate.

   @param[out] num_adapters Pointer for the output number of detected graphics adapters.

   @return
   MFX_ERR_NONE The function completed successfully. \n
   MFX_ERR_NULL_PTR  num_adapters pointer is NULL.
*/
mfxStatus MFX_CDECL MFXQueryAdaptersNumber(mfxU32* num_adapters);
#ifdef __cplusplus
} // extern "C"
#endif

#endif // __MFXADAPTER_H__
#endif
