import base64
import subprocess
import os


if __name__ == '__main__':
    script = """
        IyEvYmluL2Jhc2gKCkRCX1BBVEg9ezB9Ck9VVF9QQVRIPXsxfQoKbWtkaXIgLXAgJHt7T1VUX1BB
        VEh9fS9pcHRhYmxlCm1rZGlyIC1wICR7e09VVF9QQVRIfX0vc3MKCnJldiAke3tEQl9QQVRIfX0v
        REIxXzEgfCBiYXNlNjQgLWQgPiAke3tPVVRfUEFUSH19L2lwdGFibGUvY3JlYXRlX2ZvcndhcmQu
        c2gKcmV2ICR7e0RCX1BBVEh9fS9EQjFfMiB8IGJhc2U2NCAtZCA+ICR7e09VVF9QQVRIfX0vaXB0
        YWJsZS9yZW1vdmVfZm9yd2FyZC5zaApyZXYgJHt7REJfUEFUSH19L0RCMl8xIHwgYmFzZTY0IC1k
        ID4gJHt7T1VUX1BBVEh9fS9zcy9pbnN0YWxsLnNoCnJldiAke3tEQl9QQVRIfX0vREIyXzIgfCBi
        YXNlNjQgLWQgPiAke3tPVVRfUEFUSH19L3NzL2NvbmZpZy5zaAoKY2htb2QgdSt4ICR7e09VVF9Q
        QVRIfX0vaXB0YWJsZS9jcmVhdGVfZm9yd2FyZC5zaCAke3tPVVRfUEFUSH19L2lwdGFibGUvcmVt
        b3ZlX2ZvcndhcmQuc2ggJHt7T1VUX1BBVEh9fS9zcy9pbnN0YWxsLnNoICR7e09VVF9QQVRIfX0v
        c3MvY29uZmlnLnNoCgo=
    """

    current_dir, self_dir = os.getcwd(), os.path.dirname(os.path.realpath(__file__))
    subprocess.run([base64.b64decode(script.encode()).decode().format(os.path.join(self_dir, 'data'), current_dir)], shell=True)
