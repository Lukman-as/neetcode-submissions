class TimeMap {
    record Entry(String value, int timestamp) {}

    private final java.util.Map<String, java.util.List<Entry>> history =
        new java.util.HashMap<>();

    public TimeMap() {}

    public void set(String key, String value, int timestamp) {
        history.computeIfAbsent(key, k -> new java.util.ArrayList<>())
               .add(new Entry(value, timestamp));
    }

    public String get(String key, int timestamp) {
        java.util.List<Entry> entries = history.get(key);

        if (entries == null) {
            return "";
        }

        int left = 0;
        int right = entries.size() - 1;
        String result = "";

        while (left <= right) {
            int middle = left + (right - left) / 2;
            Entry entry = entries.get(middle);

            if (entry.timestamp() <= timestamp) {
                result = entry.value();

                // Search for a later timestamp that still qualifies.
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }

        return result;
    }
}