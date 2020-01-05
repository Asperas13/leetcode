class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        def sort_key(log):
            log_id, log_data = log.split(' ', 1)
            return (0, log_data, log_id) if log_data[0] not in digits else (1, )
        return sorted(logs, key=sort_key)