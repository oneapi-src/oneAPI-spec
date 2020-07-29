
/*############################################################################
  # Copyright (C) 2020 Intel Corporation
  #
  # SPDX-License-Identifier: MIT
  ############################################################################*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "mfxdefs.h"
#include "mfxvideo.h"
#include "mfxmvc.h"

/* these macro requires code complilation*/
#define INFINITE 0

mfxVideoParam init_param;
mfxFrameAllocRequest request;
mfxStatus sts;
mfxSession session;
mfxFrameSurface1 *surface, *surface2;
mfxBitstream *bits;
mfxSyncPoint syncp;

static void allocate_pool_of_frame_surfaces(int nFrames)
{
    return;
}

static int end_of_stream()
{
    return 1;
}

static void find_unlocked_surface_from_the_pool(mfxFrameSurface1 **pool)
{
    return;
}

static void fill_content_for_encoding(mfxFrameSurface1 *surface)
{
    return;
}

static void do_something_with_encoded_bits(mfxBitstream *bits)
{
    return;
}

static void free_pool_of_frame_surfaces()
{
    return;
}

/* end of internal stuff */

static void prg_encoding1 () {
/*beg1*/
MFXVideoENCODE_QueryIOSurf(session, &init_param, &request);
allocate_pool_of_frame_surfaces(request.NumFrameSuggested);
MFXVideoENCODE_Init(session, &init_param);
sts=MFX_ERR_MORE_DATA;
for (;;) {
   if (sts==MFX_ERR_MORE_DATA && !end_of_stream()) {
      find_unlocked_surface_from_the_pool(&surface);
      fill_content_for_encoding(surface);
   }
   surface2=end_of_stream()?NULL:surface;
   sts=MFXVideoENCODE_EncodeFrameAsync(session,NULL,surface2,bits,&syncp);
   if (end_of_stream() && sts==MFX_ERR_MORE_DATA) break;
   // Skipped other error handling
   if (sts==MFX_ERR_NONE) {
      MFXVideoCORE_SyncOperation(session, syncp, INFINITE);
      do_something_with_encoded_bits(bits);
   }
}
MFXVideoENCODE_Close(session);
free_pool_of_frame_surfaces();
/*end1*/
}

static void prg_encoding2 () {
/*beg2*/
MFXVideoENCODE_Init(session, &init_param);
sts=MFX_ERR_MORE_DATA;
for (;;) {
   if (sts==MFX_ERR_MORE_DATA && !end_of_stream()) {
      MFXMemory_GetSurfaceForEncode(session,&surface);
      fill_content_for_encoding(surface);
   }
   surface2=end_of_stream()?NULL:surface;
   sts=MFXVideoENCODE_EncodeFrameAsync(session,NULL,surface2,bits,&syncp);
   if (surface2) surface->FrameInterface->Release(surface2);
   if (end_of_stream() && sts==MFX_ERR_MORE_DATA) break;
   // Skipped other error handling
   if (sts==MFX_ERR_NONE) {
      MFXVideoCORE_SyncOperation(session, syncp, INFINITE);
      do_something_with_encoded_bits(bits);
   }
}
MFXVideoENCODE_Close(session);
/*end2*/
}

/*beg3*/
   #include "mfxvideo.h"
   #include "mfxbrc.h"

   typedef struct {
      mfxU32 EncodedOrder;
      mfxI32 QP;
      mfxU32 MaxSize;
      mfxU32 MinSize;
      mfxU16 Status;
      mfxU64 StartTime;
      // ... skipped
   } MyBrcFrame;

   typedef struct {
      MyBrcFrame* frame_queue;
      mfxU32 frame_queue_size;
      mfxU32 frame_queue_max_size;
      mfxI32 max_qp[3]; //I,P,B
      mfxI32 min_qp[3]; //I,P,B
      // ... skipped
   } MyBrcContext;

   void* GetExtBuffer(mfxExtBuffer** ExtParam, mfxU16 NumExtParam, mfxU32 bufferID)
   {
       int i=0;
       for(i = 0; i < NumExtParam; i++) {
           if(ExtParam[i]->BufferId == bufferID) return ExtParam[i];
       }
       return NULL;
   }

   static int IsParametersSupported(mfxVideoParam *par)
   {
       // do some checks
       return 1;
   }

   static int IsResetPossible(MyBrcContext* ctx, mfxVideoParam *par)
   {
       // do some checks
       return 1;
   }

   static MyBrcFrame* GetFrame(MyBrcFrame *frame_queue, mfxU32 frame_queue_size, mfxU32 EncodedOrder)
   {
       //do some logic
       if(frame_queue_size) return &frame_queue[0];
       return NULL;
   }

   static mfxU32 GetFrameCost(mfxU16 FrameType, mfxU16 PyramidLayer)
   {
       // calculate cost
       return 1;
   }

   static mfxU32 GetMinSize(MyBrcContext *ctx, mfxU32 cost)
   {
       // do some logic
       return 1;
   }

   static mfxU32 GetMaxSize(MyBrcContext *ctx, mfxU32 cost)
   {
       // do some logic
       return 1;
   }

   static mfxI32 GetInitQP(MyBrcContext *ctx, mfxU32 MinSize, mfxU32 MaxSize, mfxU32 cost)
   {
       // do some logic
       return 1;
   }

   static mfxU64 GetTime()
   {
       mfxU64 wallClock;
       return wallClock;
   }

   static void UpdateBRCState(mfxU32 CodedFrameSize, MyBrcContext *ctx)
   {
       return;
   }

   static void RemoveFromQueue(MyBrcFrame* frame_queue, mfxU32 frame_queue_size, MyBrcFrame* frame)
   {
       return;
   }

   static mfxU64 GetMaxFrameEncodingTime(MyBrcContext *ctx)
   {
       return 2;
   }

   mfxStatus MyBrcInit(mfxHDL pthis, mfxVideoParam* par) {
      MyBrcContext* ctx = (MyBrcContext*)pthis;
      mfxI32 QpBdOffset;
      mfxExtCodingOption2* co2;
      mfxI32 defaultQP;

      if (!pthis || !par)
         return MFX_ERR_NULL_PTR;

      if (!IsParametersSupported(par))
         return MFX_ERR_UNSUPPORTED;

      ctx->frame_queue_max_size = par->AsyncDepth;
      ctx->frame_queue = (MyBrcFrame*)malloc(sizeof(MyBrcFrame) * ctx->frame_queue_max_size);

      if (!ctx->frame_queue)
         return MFX_ERR_MEMORY_ALLOC;

      co2 = (mfxExtCodingOption2*)GetExtBuffer(par->ExtParam, par->NumExtParam, MFX_EXTBUFF_CODING_OPTION2);
      QpBdOffset = (par->mfx.FrameInfo.BitDepthLuma > 8) ? (6 * (par->mfx.FrameInfo.BitDepthLuma - 8)) : 0;

      ctx->max_qp[0] = (co2 && co2->MaxQPI) ? (co2->MaxQPI - QpBdOffset) : defaultQP;
      ctx->min_qp[0] = (co2 && co2->MinQPI) ? (co2->MinQPI - QpBdOffset) : defaultQP;

      ctx->max_qp[1] = (co2 && co2->MaxQPP) ? (co2->MaxQPP - QpBdOffset) : defaultQP;
      ctx->min_qp[1] = (co2 && co2->MinQPP) ? (co2->MinQPP - QpBdOffset) : defaultQP;

      ctx->max_qp[2] = (co2 && co2->MaxQPB) ? (co2->MaxQPB - QpBdOffset) : defaultQP;
      ctx->min_qp[2] = (co2 && co2->MinQPB) ? (co2->MinQPB - QpBdOffset) : defaultQP;

      // skipped initialization of other other BRC parameters

      ctx->frame_queue_size = 0;

      return MFX_ERR_NONE;
   }

   mfxStatus MyBrcReset(mfxHDL pthis, mfxVideoParam* par) {
      MyBrcContext* ctx = (MyBrcContext*)pthis;

      if (!pthis || !par)
         return MFX_ERR_NULL_PTR;

      if (!IsParametersSupported(par))
         return MFX_ERR_UNSUPPORTED;

      if (!IsResetPossible(ctx, par))
         return MFX_ERR_INCOMPATIBLE_VIDEO_PARAM;

      // reset here BRC parameters if required

      return MFX_ERR_NONE;
   }

   mfxStatus MyBrcClose(mfxHDL pthis) {
      MyBrcContext* ctx = (MyBrcContext*)pthis;

      if (!pthis)
         return MFX_ERR_NULL_PTR;

      if (ctx->frame_queue) {
         free(ctx->frame_queue);
         ctx->frame_queue = NULL;
         ctx->frame_queue_max_size = 0;
         ctx->frame_queue_size = 0;
      }

      return MFX_ERR_NONE;
   }

   mfxStatus MyBrcGetFrameCtrl(mfxHDL pthis, mfxBRCFrameParam* par, mfxBRCFrameCtrl* ctrl) {
      MyBrcContext* ctx = (MyBrcContext*)pthis;
      MyBrcFrame* frame = NULL;
      mfxU32 cost;

      if (!pthis || !par || !ctrl)
         return MFX_ERR_NULL_PTR;

      if (par->NumRecode > 0)
         frame = GetFrame(ctx->frame_queue, ctx->frame_queue_size, par->EncodedOrder);
      else if (ctx->frame_queue_size < ctx->frame_queue_max_size)
         frame = &ctx->frame_queue[ctx->frame_queue_size++];

      if (!frame)
         return MFX_ERR_UNDEFINED_BEHAVIOR;

      if (par->NumRecode == 0) {
         frame->EncodedOrder = par->EncodedOrder;
         cost = GetFrameCost(par->FrameType, par->PyramidLayer);
         frame->MinSize = GetMinSize(ctx, cost);
         frame->MaxSize = GetMaxSize(ctx, cost);
         frame->QP = GetInitQP(ctx, frame->MinSize, frame->MaxSize, cost); // from QP/size stat
         frame->StartTime = GetTime();
      }

      ctrl->QpY = frame->QP;

      return MFX_ERR_NONE;
   }

   #define DEFAULT_QP_INC 4
   #define DEFAULT_QP_DEC 4

   mfxStatus MyBrcUpdate(mfxHDL pthis, mfxBRCFrameParam* par, mfxBRCFrameCtrl* ctrl, mfxBRCFrameStatus* status) {
      MyBrcContext* ctx = (MyBrcContext*)pthis;
      MyBrcFrame* frame = NULL;
      mfxU32 panic = 0;

      if (!pthis || !par || !ctrl || !status)
         return MFX_ERR_NULL_PTR;

      frame = GetFrame(ctx->frame_queue, ctx->frame_queue_size, par->EncodedOrder);
      if (!frame)
         return MFX_ERR_UNDEFINED_BEHAVIOR;

      // update QP/size stat here

      if (   frame->Status == MFX_BRC_PANIC_BIG_FRAME
        || frame->Status == MFX_BRC_PANIC_SMALL_FRAME)
         panic = 1;

      if (panic || (par->CodedFrameSize >= frame->MinSize && par->CodedFrameSize <= frame->MaxSize)) {
         UpdateBRCState(par->CodedFrameSize, ctx);
         RemoveFromQueue(ctx->frame_queue, ctx->frame_queue_size, frame);
         ctx->frame_queue_size--;
         status->BRCStatus = MFX_BRC_OK;

         // Here update Min/MaxSize for all queued frames

         return MFX_ERR_NONE;
      }

      panic = ((GetTime() - frame->StartTime) >= GetMaxFrameEncodingTime(ctx));

      if (par->CodedFrameSize > frame->MaxSize) {
         if (panic || (frame->QP >= ctx->max_qp[0])) {
            frame->Status = MFX_BRC_PANIC_BIG_FRAME;
         } else {
            frame->Status = MFX_BRC_BIG_FRAME;
            frame->QP = DEFAULT_QP_INC;
         }
      }

      if (par->CodedFrameSize < frame->MinSize) {
         if (panic || (frame->QP <= ctx->min_qp[0])) {
            frame->Status = MFX_BRC_PANIC_SMALL_FRAME;
            status->MinFrameSize = frame->MinSize;
         } else {
            frame->Status = MFX_BRC_SMALL_FRAME;
            frame->QP = DEFAULT_QP_DEC;
         }
      }

      status->BRCStatus = frame->Status;

      return MFX_ERR_NONE;
   }

   void EncoderInit()
   {
        //initialize encoder
        MyBrcContext brc_ctx;
        mfxExtBRC ext_brc;
        mfxExtCodingOption2 co2;
        mfxExtBuffer* ext_buf[2] = {&co2.Header, &ext_brc.Header};
        mfxVideoParam vpar;

        memset(&brc_ctx, 0, sizeof(MyBrcContext));
        memset(&ext_brc, 0, sizeof(mfxExtBRC));
        memset(&co2, 0, sizeof(mfxExtCodingOption2));

        vpar.ExtParam = ext_buf;
        vpar.NumExtParam = sizeof(ext_buf) / sizeof(ext_buf[0]);

        co2.Header.BufferId = MFX_EXTBUFF_CODING_OPTION2;
        co2.Header.BufferSz = sizeof(mfxExtCodingOption2);
        co2.ExtBRC = MFX_CODINGOPTION_ON;

        ext_brc.Header.BufferId = MFX_EXTBUFF_BRC;
        ext_brc.Header.BufferSz = sizeof(mfxExtBRC);
        ext_brc.pthis           = &brc_ctx;
        ext_brc.Init            = MyBrcInit;
        ext_brc.Reset           = MyBrcReset;
        ext_brc.Close           = MyBrcClose;
        ext_brc.GetFrameCtrl    = MyBrcGetFrameCtrl;
        ext_brc.Update          = MyBrcUpdate;

        sts = MFXVideoENCODE_Query(session, &vpar, &vpar);
        if (sts == MFX_ERR_UNSUPPORTED || co2.ExtBRC != MFX_CODINGOPTION_ON)
            // unsupported case
            sts = sts;
        else
            sts = MFXVideoENCODE_Init(session, &vpar);
   }
/*end3*/

static void prg_encoding4 () {
/*beg4*/
mfxExtBuffer *eb;
mfxExtMVCSeqDesc  seq_desc;
mfxVideoParam init_param;

init_param.ExtParam=(mfxExtBuffer **)&eb;
init_param.NumExtParam=1;
eb=(mfxExtBuffer *)&seq_desc;

/* init encoder */
MFXVideoENCODE_Init(session, &init_param);

/* perform encoding */
for (;;) {
    MFXVideoENCODE_EncodeFrameAsync(session, NULL, surface2, bits,
                                    &syncp);
    MFXVideoCORE_SyncOperation(session,syncp,INFINITE);
}

/* close encoder */
MFXVideoENCODE_Close(session);
/*end4*/
}