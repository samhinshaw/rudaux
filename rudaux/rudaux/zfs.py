from subprocess import check_output, STDOUT
import os

class ZFS(object):
    """
    Interface to ZFS commands
    """

    def __init__(self, course):
        self.user_folder_root = course.config.user_folder_root
        self.dry_run = course.dry_run

    def snapshot_all(self, snap_name):
        cmd_list = ['zfs', 'snapshot', '-r', self.jupyterhub_user_folder_root.strip('/') + '@'+snap_name]
        if not self.dry_run:
            check_output(cmd_list, stderr=STDOUT)
        else:
            print('[Dry run: would have called: ' + ' '.join(cmd_list) + ']')

    def snapshot_user(self, user, snap_name):
        cmd_list = ['zfs', 'snapshot', os.path.join(self.jupyterhub_user_folder_root, user).strip('/') + '@'+snap_name]
        if not self.dry_run:
            check_output(cmd_list, stderr=STDOUT)
        else:
            print('[Dry run: would have called: ' + ' '.join(cmd_list) + ']')

    def list_snapshots(self):
        print(check_output(['zfs', 'list', '-t', 'snapshot'], stderr = STDOUT))

    def create_user_folder(self, username):
        callysto_user = 'jupyter'
        course = 'dsci100'
        cmd_list = [os.path.join(self.jupyterhub_config_dir, 'zfs_homedir.sh'), course, username, callysto_user]
        if not self.dry_run:
            check_output(cmd_list, stderr=STDOUT)
        else:
            print('[Dry run: would have called: ' + ' '.join(cmd_list) + ']')
 
