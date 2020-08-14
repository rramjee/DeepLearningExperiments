import torch
import torch.nn.functional as F

def gradient_loss(gen_frames, gt_frames, alpha=1):

    def gradient(x):
        # idea from tf.image.image_gradients(image)
        # https://github.com/tensorflow/tensorflow/blob/r2.1/tensorflow/python/ops/image_ops_impl.py#L3441-L3512
        # x: (b,c,h,w), float32 or float64
        # dx, dy: (b,c,h,w)

        h_x = x.size()[-2]
        w_x = x.size()[-1]
        # gradient step=1
        left = x
        right = F.pad(x, [0, 1, 0, 0])[:, :, :, 1:]
        top = x
        bottom = F.pad(x, [0, 0, 0, 1])[:, :, 1:, :]

        # dx, dy = torch.abs(right - left), torch.abs(bottom - top)
        dx, dy = right - left, bottom - top 
        # dx will always have zeros in the last column, right-left
        # dy will always have zeros in the last row,    bottom-top
        dx[:, :, :, -1] = 0
        dy[:, :, -1, :] = 0

        return dx, dy

    # gradient
    gen_dx, gen_dy = gradient(gen_frames)
    gt_dx, gt_dy = gradient(gt_frames)
    #
    grad_diff_x = torch.abs(gt_dx - gen_dx)
    grad_diff_y = torch.abs(gt_dy - gen_dy)

    # condense into one tensor and avg
    return torch.mean(grad_diff_x ** alpha + grad_diff_y ** alpha)


def depth_loss(preddepth, depthmap, ssimloss, theta = 0.1):

  #Calculate Pixel wise Depth Loss
  depth_loss = torch.mean(torch.abs(preddepth - depthmap))

  #Calcualte Gradient Loss
  grad_loss_term = gradient_loss(preddepth, depthmap)

  #Calculate SSIM loss
  ssim_loss = ssimloss(preddepth, depthmap)

  # Weights
  w1 = 1.0
  w2 = 1.0
  w3 = theta

  return (w1 * ssim_loss) + (w2 * grad_loss_term) + (w3 * depth_loss)
