.. _vid_process_procedure:

===========================
Video Processing Procedures
===========================

The following example shows the pseudo code of the video processing procedure:

.. literalinclude:: snippets/prg_vpp.c
   :language: c++
   :start-after: /*beg1*/
   :end-before: /*end1*/
   :lineno-start: 1

Note the following key points about the example:

- The application uses the :cpp:func:`MFXVideoVPP_QueryIOSurf` function to
  obtain the number of frame surfaces needed for input and output. The application
  must allocate two frame surface pools: one for the input and one for the output.
- The video processing function :cpp:func:`MFXVideoVPP_RunFrameVPPAsync` is
  asynchronous. The application must use the :cpp:func:`MFXVideoCORE_SyncOperation`
  function to synchronize to make the output result ready.
- The body of the video processing procedure covers the following three scenarios:

  - If the number of frames consumed at input is equal to the number of frames
    generated at output, :term:`VPP` returns :cpp:enumerator:`mfxStatus::MFX_ERR_NONE` when an
    output is ready. The application must process the output frame after
    synchronization, as the :cpp:func:`MFXVideoVPP_RunFrameVPPAsync` function is
    asynchronous. The application must provide a NULL input at the end of the
    sequence to drain any remaining frames.
  - If the number of frames consumed at input is more than the number of frames
    generated at output, VPP returns :cpp:enumerator:`mfxStatus::MFX_ERR_MORE_DATA` for
    additional input until an output is ready. When the output is ready, VPP
    returns :cpp:enumerator:`mfxStatus::MFX_ERR_NONE`. The application must process the
    output frame after synchronization and provide a NULL input at the end of the
    sequence to drain any remaining frames.
  - If the number of frames consumed at input is less than the number of frames
    generated at output, VPP returns either :cpp:enumerator:`mfxStatus::MFX_ERR_MORE_SURFACE`
    (when more than one output is ready), or :cpp:enumerator:`mfxStatus::MFX_ERR_NONE`
    (when one output is ready and VPP expects new input). In both cases, the
    application must process the output frame after synchronization and provide
    a NULL input at the end of the sequence to drain any remaining frames.

-------------
Configuration
-------------

The SDK configures the video processing pipeline operation based on the
difference between the input and output formats, specified in the
:cpp:struct:`mfxVideoParam` structure. The following list shows several examples:

- When the input color format is :term:`YUY2` and the output color format is
  :term:`NV12`, the SDK enables color conversion from YUY2 to NV12.
- When the input is interleaved and the output is progressive, the SDK enables
  deinterlacing.
- When the input is single field and the output is interlaced or progressive,
  the SDK enables field weaving, optionally with deinterlacing.
- When the input is interlaced and the output is single field, the SDK enables
  field splitting.

In addition to specifying the input and output formats, the application can
provide hints to fine-tune the video processing pipeline operation. The
application can disable filters in the pipeline by using the
:cpp:struct:`mfxExtVPPDoNotUse` structure, enable filters by using the
:cpp:struct:`mfxExtVPPDoUse` structure, and configure filters by using dedicated
configuration structures. See the :ref:`Configurable VPP Filters table <vpp-filters-table>`
for a complete list of configurable video processing filters, their IDs, and
configuration structures. See the :ref:`ExtendedBufferID enumerator <extendedbufferid>`
for more details.

The SDK ensures that all filters necessary to convert the input format to the
output format are included in the pipeline. The SDK may skip some optional
filters even if they are explicitly requested by the application, for example,
due to limitations of the underlying hardware. To notify the application about
skipped optional filters, the SDK returns the :cpp:enumerator:`mfxStatus::MFX_WRN_FILTER_SKIPPED`
warning. The application can retrieve the list of active filters by attaching
the :cpp:struct:`mfxExtVPPDoUse` structure to the :cpp:struct:`mfxVideoParam`
structure and calling the :cpp:func:`MFXVideoVPP_GetVideoParam` function. The
application must allocate enough memory for the filter list.

See the :ref:`Configurable VPP Filters table <vpp-filters-table>` for a full
list of configurable filters.

.. _vpp-filters-table:

.. table:: Configurable VPP Filters

   ======================================  ==========================================
   Filter ID                               Configuration Structure
   ======================================  ==========================================
   MFX_EXTBUFF_VPP_DENOISE                 :cpp:struct:`mfxExtVPPDenoise`
   MFX_EXTBUFF_VPP_MCTF                    :cpp:struct:`mfxExtVppMctf`
   MFX_EXTBUFF_VPP_DETAIL                  :cpp:struct:`mfxExtVPPDetail`
   MFX_EXTBUFF_VPP_FRAME_RATE_CONVERSION   :cpp:struct:`mfxExtVPPFrameRateConversion`
   MFX_EXTBUFF_VPP_IMAGE_STABILIZATION     :cpp:struct:`mfxExtVPPImageStab`
   MFX_EXTBUFF_VPP_PICSTRUCT_DETECTION     none
   MFX_EXTBUFF_VPP_PROCAMP                 :cpp:struct:`mfxExtVPPProcAmp`
   MFX_EXTBUFF_VPP_FIELD_PROCESSING        :cpp:struct:`mfxExtVPPFieldProcessing`
   ======================================  ==========================================

The following example shows video processing configuration:

.. literalinclude:: snippets/prg_vpp.c
   :language: c++
   :start-after: /*beg2*/
   :end-before: /*end2*/
   :lineno-start: 1

------------------
Region of Interest
------------------

During video processing operations, the application can specify a region of
interest for each frame as shown in the following image:

.. image:: images/vpp_region_of_interest_operation.png
   :alt: VPP Region of Interest Operation

Specifying a region of interest guides the resizing function to achieve special
effects, such as resizing from 16:9 to 4:3, while keeping the aspect ratio intact.
Use the ``CropX``, ``CropY``, ``CropW``, and ``CropH`` parameters in the
:cpp:struct:`mfxVideoParam` structure to specify a region of interest.

The :ref:`VPP Region of Interest Operations table <vpp-region-op-table>` shows
examples of VPP operations applied to a region of interest.

.. _vpp-region-op-table:

.. table:: VPP Region of Interest Operations

   +-----------------------+------------------+-------------------+------------------+--------------------+
   | **Operation**         | **VPP Input**    | **VPP Input**     | **VPP Output**   | **VPP Output**     |
   |                       | *Width x Height* | *CropX, CropY,*   | *Width x Height* | *CropX, CropY,*    |
   |                       |                  | *CropW, CropH*    |                  | *CropW, CropH*     |
   +-----------------------+------------------+-------------------+------------------+--------------------+
   | Cropping              | 720 x 480        | 16, 16, 688, 448  | 720 x 480        | 16, 16, 688, 448   |
   +-----------------------+------------------+-------------------+------------------+--------------------+
   | Resizing              | 720 x 480        | 0, 0, 720, 480    | 1440 x 960       | 0, 0, 1440, 960    |
   +-----------------------+------------------+-------------------+------------------+--------------------+
   | Horizontal stretching | 720 x 480        | 0, 0, 720, 480    | 640 x 480        | 0, 0, 640, 480     |
   +-----------------------+------------------+-------------------+------------------+--------------------+
   | 16:9 4:3 with letter  | 1920 x 1088      | 0, 0, 1920, 1088  | 720 x 480        | 0, 36, 720, 408    |
   | boxing at the top and |                  |                   |                  |                    |
   | bottom                |                  |                   |                  |                    |
   +-----------------------+------------------+-------------------+------------------+--------------------+
   | 4:3 16:9 with pillar  | 720 x 480        | 0, 0, 720, 480    | 1920 x 1088      | 144, 0, 1632, 1088 |
   | boxing at the left    |                  |                   |                  |                    |
   | and right             |                  |                   |                  |                    |
   +-----------------------+------------------+-------------------+------------------+--------------------+

---------------------------
Multi-view Video Processing
---------------------------

SDK video processing supports processing multiple views. For video processing
initialization, the application needs to attach the :cpp:struct:`mfxExtMVCSeqDesc`
structure to the :cpp:struct:`mfxVideoParam` structure and call the
:cpp:func:`MFXVideoVPP_Init` function. The function saves the view identifiers.
During video processing, the SDK processes each view individually. The SDK refers
to the FrameID field of the :cpp:struct:`mfxFrameInfo` structure to configure
each view according to its processing pipeline. If the video processing source
frame is not the output from the SDK MVC decoder, then the application needs to
fill the the FrameID field before calling the :cpp:func:`MFXVideoVPP_RunFrameVPPAsync`
function. This is shown in the following pseudo code:

.. literalinclude:: snippets/prg_vpp.c
   :language: c++
   :start-after: /*beg3*/
   :end-before: /*end3*/
   :lineno-start: 1