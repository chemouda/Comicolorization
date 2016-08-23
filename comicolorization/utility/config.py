import argparse
import typing


def get_train_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("dataset_path")
    parser.add_argument("save_result_path")
    parser.add_argument("--network_model", required=True, type=str)
    parser.add_argument('--num_dataset_test', required=True, type=int)
    parser.add_argument("--batchsize", type=int, default=5)
    parser.add_argument("--size_image", type=int, default=128)
    parser.add_argument("--augmentation", type=bool, default=False)
    parser.add_argument("--size_image_augmentation", type=int, default=None)
    parser.add_argument('--gpu', type=int, default=-1)
    parser.add_argument('--max_epoch', type=int, default=1000)
    parser.add_argument('--save_result_iteration', type=int, default=100)
    parser.add_argument('--random_seed_test', type=int, default=None)
    parser.add_argument('--path_pretrained_model', default=None)
    parser.add_argument('--disable_ltbc_global', action='store_true')
    parser.add_argument('--line_drawing_mode', type=str, choices=['otsu_threshold', 'adaptive_threshold', 'canny', 'three_value_threshold', 'dilate-diff'], default=None)
    parser.add_argument('--weight_decay', type=float, default=None)
    parser.add_argument('--path_tag_list', type=str)
    parser.add_argument('--path_tag_list_each_image', type=str)
    parser.add_argument('--blend_mse_color', type=float, default=1.0)
    parser.add_argument('--alpha_ltbc_classification', type=float, default=None)
    parser.add_argument('--ltbc_classification_num_output_list', type=int, nargs='+', default=[256, 205])
    parser.add_argument('--use_histogram_network', action='store_true')
    parser.add_argument('--num_bins_histogram', type=int, default=85)
    parser.add_argument('--threshold_histogram_palette', type=float, default=None)
    parser.add_argument('--use_multidimensional_histogram', action='store_true')
    parser.add_argument('--reinput_mode', type=str, choices=['color'], default=None)
    parser.add_argument('--loss_blend_ratio_reinput', type=float, nargs='+', default=[])
    parser.add_argument('--separate_backward_reinput', action='store_true')
    parser.add_argument('--separate_model_reinput', action='store_true')
    parser.add_argument('--use_residual_reinput', action='store_true')
    parser.add_argument('--ltbc_classification_loss_function', type=str, choices=['softmax', 'multi_label'], default='softmax')
    parser.add_argument('--max_pixel_drawing', type=int, default=None)
    parser.add_argument('--max_size_pixel_drawing', type=int, default=1)
    parser.add_argument('--loss_type', type=str, default='RGB')
    parser.add_argument('--mse_loss_mode', choices=['color_space', 'before_sigmoid'], default='color_space')
    parser.add_argument('--use_adversarial_network', action='store_true')
    parser.add_argument('--blend_adversarial_generator', type=float, default=1.0)
    parser.add_argument('--discriminator_first_pooling_size', type=int, default=1)
    parser.add_argument('--log_interval', type=int, default=10, help="number of logging interval iterations")
    return parser


def get_default_train_args() -> typing.Dict[str, object]:
    parser = get_train_parser()
    args = parser.parse_args('dummy dummy --network_model dummy --num_dataset_test 0'.split())
    return args.__dict__


def get_predict_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths_result_directory", nargs='+')
    parser.add_argument("--path_root", type=str)
    parser.add_argument("--num_image", type=int, default=10)
    parser.add_argument("--dirname_save_images", type=str, default='images_with_trained_model')
    parser.add_argument("--gpu", type=int, default=-1)
    parser.add_argument("--prefix_save_filename", type=str, default='')
    parser.add_argument("--test_dataset_path", help="if unspecified, then use same as training")
    parser.add_argument("--num_rebalance_hist_rate_split", type=int, default=0)
    parser.add_argument("--loss_type", help="if unspecified, then use same as training")
    parser.add_argument("--scale_input", type=float, default=1.0, help="scaling of input value range")
    parser.add_argument("--target_iteration", nargs='+', type=int, help="if unspecified, target all iteration")
    parser.add_argument("--binarization_input", action='store_true', help="binarization input image")
    parser.add_argument("--direct_input", action='store_true')
    parser.add_argument("--use_binarization_dataset", action='store_true')
    parser.add_argument("--save_grayimage_color_normalized", action='store_true')
    parser.add_argument("--reference_image_path", nargs='+')
    return parser
